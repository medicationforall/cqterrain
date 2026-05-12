# Copyright 2026 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import cadquery as cq
from cadqueryhelper import Base
from cadqueryhelper.shape import trapezoid

class Shutter(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 25
        self.width:float = 2
        self.height:float = 30
        self.louver_count:float  = 5
        self.louver_rotate:float  = 16
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.louver:cq.Workplane|None = None
        self.flat_louver:cq.Workplane|None = None
        self.louvers:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_louver(self):
        height = self.height / self.louver_count
        
        louver = cq.Workplane("XY").box(
            self.length,
            self.width,
            height
        )
        
        flat_louver = cq.Workplane("XY").box(
            self.length,
            self.width,
            height
        )
        
        overlap_height = height / 2
        overlap_length = self.length / 2
        overlap_bottom_length = overlap_length - 3
        overlap = trapezoid(length = self.width,
            width = overlap_bottom_length,
            height = overlap_height,
            top_width = overlap_length
        )
        
        louver = louver.union(overlap.translate((0,0,-height/2-overlap_height/2)))
        
        louver = louver.rotate((1,0,0),(0,0,0),self.louver_rotate)
        flat_louver = flat_louver.rotate((1,0,0),(0,0,0),self.louver_rotate)
        
        self.louver = louver
        self.flat_louver = flat_louver
        
    def make_louvers(self):
        height = self.height / self.louver_count
        louvers = cq.Workplane("XY")
        for i in range(self.louver_count):
            if i == 0:
                louvers = louvers.add(self.flat_louver.translate((0,0,height*i)))
                continue
            louvers = louvers.add(self.louver.translate((0,0,height*i)))
        
        self.louvers = louvers.translate((0,0,height/2-self.height/2))
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_louver()
        self.make_louvers()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        #if self.outline:
        #    part = part.add(self.outline)
        
        #if self.louver:
        #    part = part.add(self.louver)
            
        if self.louvers:
            part = part.union(self.louvers)
        
        return part
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

class BaseWall(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 75
        self.width:float = 4
        self.height:float = 75
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.wall:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_wall(self):
        length = self.length
        width = self.width
        height = self.height
        wall = cq.Workplane("XY").box(length,width,height)
        self.wall = wall
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_wall()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.wall:
            part = part.add(self.wall)
        
        return part
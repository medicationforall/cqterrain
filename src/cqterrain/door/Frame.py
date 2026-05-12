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

class Frame(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 60
        self.width:float = 3
        self.height:float = 40
        
        self.frame_width:float = 3
        self.chamfer:float = 5
        self.cut_chamfer:float = 3.5
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.frame:cq.Workplane|None = None
        self.frame_cut:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_frame(self):
        frame = (
            cq.Workplane("XY").box(
                self.length,
                self.width,
                self.height
            )
            .faces("Z")
            .edges("|Y")
            .chamfer(self.chamfer)
        )
        
        self.frame = frame
        
    def make_frame_cut(self):
        length = self.length - self.frame_width*2
        width = self.width
        height = self.height - self.frame_width
        frame_cut = (
            cq.Workplane("XY").box(
                length,
                width,
                height
            )
            .faces("Z")
            .edges("|Y")
            .chamfer(self.cut_chamfer)
            .translate((0,0,-self.frame_width/2))
        )
        
        self.frame_cut = frame_cut
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_frame()
        self.make_frame_cut()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.frame:
            part = part.union(self.frame)
            
        if self.frame_cut:
            part =  part.cut(self.frame_cut)
        
        return part.translate((0,0,self.height/2))
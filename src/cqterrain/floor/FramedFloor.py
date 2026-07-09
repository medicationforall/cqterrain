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

class FramedFloor(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 75
        self.width:float = 75
        self.height:float = 4
        self.frame_width:float = 2
        self.corner_chamfer:float|None = 8
        self.corner_fillet:float|None = None
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.frame_cut:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_frame_cut(self):
        length = self.length - self.frame_width*2
        width = self.width - self.frame_width*2
        height = self.height
        frame_cut = cq.Workplane("XY").box(length,width,height)
        
        if self.corner_chamfer:
            frame_cut = frame_cut.edges("|Z").chamfer(self.corner_chamfer)
        elif self.corner_fillet:
            frame_cut = frame_cut.edges("|Z").fillet(self.corner_fillet)
        
        self.frame_cut = frame_cut
        
    def make(self):
        super().make()
        self.make_outline()
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
        
        if self.outline:
            part = part.add(self.outline)
            
        if self.frame_cut:
            part = part.cut(self.frame_cut)
        
        return part
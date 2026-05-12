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
from . import Shutter

class ShutterWindow(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 50
        self.width:float = 4
        self.height:float = 25
        
        self.frame_width:float = 4
        self.pane_count:int = 2
        self.louver_count:int = 5
        self.louver_rotate:float = 16
        
        # blueprints
        self.bp_shutter:Base = Shutter()
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.frame:cq.Workplane|None = None
        self.pane:cq.Workplane|None = None
        self.panes:cq.Workplane|None = None
        self.divider:cq.Workplane|None = None
        self.pane_dividers:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_frame(self):
        body = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        ).faces(">Z").edges("|Y").chamfer(self.frame_width);
        
        frame_cut = cq.Workplane("XY").box(
            self.length - self.frame_width*2,
            self.width,
            self.height - self.frame_width*2
        )
        
        self.frame = body.cut(frame_cut)
        
    def make_panes(self):
        inner_length = self.length
        length = inner_length / self.pane_count
        
        self.bp_shutter.length = length-self.frame_width-self.frame_width/2
        self.bp_shutter.louver_count = self.louver_count
        self.bp_shutter.louver_rotate = self.louver_rotate
        self.bp_shutter.height = self.height-self.frame_width*2
        self.bp_shutter.make()
        pane = self.bp_shutter.build()
        
        
        self.bp_shutter.length = length-self.frame_width
        self.bp_shutter.make()
        inner_pane = self.bp_shutter.build()
        
        panes = cq.Workplane("XY")
        
        for i in range(self.pane_count):
            if i == 0:
                panes = panes.add(pane.translate((length*i+self.frame_width/4,0,0)))
            elif i == self.pane_count-1:
                 panes = panes.add(pane.translate((length*i-self.frame_width/4,0,0)))
            else:
                panes = panes.add(inner_pane.translate((length*i,0,0)))
        
        self.panes = panes.translate((length/2 - inner_length/2,0,0))
        
    def make_divider(self):
        div_height = self.height-self.frame_width*2
        divider = cq.Workplane("XY").box(
            self.frame_width,
            self.width,
            div_height
            
        )
        
        diameter = self.frame_width/2
        z_translate = div_height/2-diameter/2 - self.frame_width/2
        circle = cq.Workplane("ZX").cylinder(self.width/2,diameter/2)
        circles = (
            cq.Workplane("XY")
            .add(circle.translate((0,0,z_translate)))
            .add(circle.translate((0,0,-z_translate)))
        )
        
        y_translate = self.width/2
        self.divider = (
            divider
            .cut(circles.translate((0,y_translate,0)))
            .cut(circles.translate((0,-y_translate,0)))
        )
        
    def make_divider_alt(self):
        divider = cq.Workplane("XY").box(
            self.frame_width,
            self.width,
            self.height-self.frame_width*2
        )
        
        circle = cq.Workplane("ZX").cylinder(self.width,4)
        
        self.divider = divider.add(circle)
        
    def make_pane_dividers(self):
        length = self.length / self.pane_count
        divider = self.divider
        
        panes = cq.Workplane("XY")
        
        for i in range(self.pane_count-1):
            panes = panes.add(divider.translate((length*i,0,0)))
        
        self.pane_dividers = panes.translate((length - self.length/2,0,0))
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_frame()
        self.make_panes()
        self.make_divider()
        self.make_pane_dividers()
        
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
            part = part.add(self.frame)
            
        if self.pane_dividers and self.pane_count >1:
            part = part.union(self.pane_dividers)
            
        if self.panes:
            part = part.union(self.panes)
        
        return part
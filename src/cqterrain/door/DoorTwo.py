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
from cadqueryhelper.shape import trapezoid
from cadqueryhelper import Base

class DoorTwo(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 30
        self.width:float = 2
        self.height:float = 40
        
        self.greeble_length:float = 5
        self.greeble_width:float = 3
        self.greeble_height:float = 12
        self.greeble_inner_height:float = 4
        self.greeble_z_translate:float = -3
        
        self.chamfer:tuple[float|None,float|None] = (3.5,3.5)
        self.side_chamfer:float|None = .5
        
        self.render_window:bool = True
        self.window_length:float = 6
        self.window_width:float = 3
        self.window_height:float = 3
        self.window_frame_width:float = 1
        self.window_z_translate:float = 30
        
        self.hinge_offset:float = 3
        self.hinge_chamfer:float = 1
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.greeble:cq.Workplane|None = None
        self.door:cq.Workplane|None = None
        self.window:cq.Workplane|None = None
        self.window_cut:cq.Workplane|None = None
        self.hinge:cq.Workplane|None = None
        self.hinges:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_frame_greeble(self):
        length = self.length
        g_length = self.greeble_length
        g_width = self.greeble_width
        result = (
            trapezoid(
                length = g_width,
                width = self.greeble_height,
                height = g_length,
                top_width = self.greeble_inner_height
            )
            .rotate((0,1,0),(0,0,0),90)
            .translate((length/2-g_length/2,0,0))
        )

        if self.side_chamfer:
            result = result.translate((-self.side_chamfer,0,self.greeble_z_translate))
        else:
            result = result.translate((0,0,self.greeble_z_translate))

        self.greeble = result
        
    def make_door(self):
        length = self.length
        width = self.width
        height = self.height
        door = (
            cq.Workplane("XY")
            .box(
                length,
                width,
                height
            )
        )
        
        i_door = (
            cq.Workplane("XY")
            .box(
                length,
                width,
                height
            )
        )
        
        if(self.chamfer[0]):
            door = (
                door
                .faces("Z")
                .edges("<X")
                .chamfer(self.chamfer[0])
            )
        
        if(self.chamfer[1]):
            door = (
                door
                .faces("Z")
                .edges(">X")
                .chamfer(self.chamfer[1])
            )
            
        if self.side_chamfer:
            i_door = (
                i_door
                .faces(">X")
                .edges("|Z")
                .chamfer(self.side_chamfer)
            )
            
        self.door = i_door.intersect(door)
        
    def make_window(self):
        door_height = self.height
        window = (
            cq.Workplane("XY")
            .box(
                self.window_length,
                self.window_width,
                self.window_height
            )
            .translate((0,0,-door_height/2))
        )
        
        self.window = window.translate((0,0,self.window_z_translate))
        
    def make_window_cut(self):
        door_height = self.height
        length = self.window_length - self.window_frame_width*2
        width = self.window_width
        height = self.window_height - self.window_frame_width*2
        window = (
            cq.Workplane("XY")
            .box(
                length,
                width,
                height
            )
            .translate((0,0,-door_height/2))
        )
        
        self.window_cut = window.translate((0,0,self.window_z_translate))

    def make_hinge(self):
        h_length = 3
        g_width = self.greeble_width
        h_height = 5
        hinge = cq.Workplane("XY").box(3,g_width,h_height)
        
        if self.hinge_chamfer:
            hinge = hinge.faces(">X").edges("|Y").chamfer(self.hinge_chamfer)
        
        
        self.hinge = hinge.translate((-self.length/2+h_length/2,0,0))
        
    def make_hinges(self):
        h_height = 5
        z_translate_top = self.height/2 - h_height/2 - self.chamfer[0] - self.hinge_offset
        z_translate_bottom = -self.height/2 + h_height/2 + self.hinge_offset
        hinges = (
            cq.Workplane("XY")
            .add(self.hinge.translate((0,0,z_translate_top)))
            .add(self.hinge.translate((0,0,z_translate_bottom)))
        )
        
        self.hinges = hinges
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_frame_greeble()
        self.make_door()
        self.make_window()
        self.make_window_cut()
        self.make_hinge()
        self.make_hinges()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.door:
            part = part.union(self.door)
            
        if self.greeble:
            part = part.union(self.greeble)
            
        if self.render_window and self.window:
            part = part.union(self.window)
            
        if self.render_window and self.window_cut:
            part = part.cut(self.window_cut)
            
        if self.hinges:
            part = part.union(self.hinges)
        
        return part.translate((0,0,self.height/2))
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
from . import Frame
from . import DoorTwo


class DoorDouble(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 60
        self.width:float = 3
        self.height:float = 40

        self.frame_width:float = 3
        self.chamfer:float = 5
        self.cut_chamfer:float = 3.5
        
        self.window_length:float = 6
        self.window_height:float = 3
        self.window_z_translate:float = 30
        
        # blueprints
        self.bp_frame:cq.Workplane|None = Frame()
        self.bp_door:cq.Workplane|None = DoorTwo()
        
        #shapes
        self.outline:cq.Workplane|None = None
        
    def calculate_internal_length(self):
        return self.length - self.frame_width * 2
    
    def calculate_internal_height(self):
        return self.height - self.frame_width
    
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_frame(self):
        self.bp_frame.length = self.length
        self.bp_frame.width = self.width
        self.bp_frame.height = self.height
        
        self.bp_frame.make()
        
        
    def make_door(self):
        internal_length = self.calculate_internal_length()
        internal_height = self.calculate_internal_height()
        
        self.bp_door.length = internal_length/2
        self.bp_door.height = internal_height
        self.bp_door.window_length = self.window_length
        self.bp_door.window_height = self.window_height
        self.bp_door.window_z_translate = self.window_z_translate
        self.bp_door.chamfer= (self.cut_chamfer,0)
        self.bp_door.make()
        

    def make(self):
        super().make()
        self.make_outline()
        self.make_frame()
        self.make_door()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bp_frame:
            frame = self.bp_frame.build()
            part = part.union(frame)
            
            
        if self.bp_door:
            internal_length = self.calculate_internal_length()
            x_translate = -internal_length /2 + self.bp_door.length/2

            door = (
                self.bp_door.build()
                .translate((x_translate,0,0))
            )
            
            part = (
                part
                .add(door)
                .add(door.rotate((0,0,1),(0,0,0),180))
            )
        
        return part
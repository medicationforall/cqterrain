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
from ..wall import BaseWall
from ..floor import BaseFloor


class BaseSegment(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 75
        self.width:float = 75
        self.height:float = 75
        
        self.floor_height:float = 6
        self.wall_width:float = 4
        
        # blueprints
        self.bp_wall:BaseWall = BaseWall()
        self.bp_floor:BaseFloor = BaseFloor()
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.floor_fill = None
        
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_wall(self):
        if self.bp_wall:
            height = self.height - self.floor_height
            self.bp_wall.height = height
            self.bp_wall.make()
            
            
    def make_floor(self):
        if self.bp_floor:
            length = self.length
            width = self.width - self.bp_wall.width
            height = self.floor_height
            self.bp_floor.length = length
            self.bp_floor.width = width
            self.bp_floor.height = height
            self.bp_floor.make()
            
    def make_floor_fill(self):
        length = self.length
        width = self.bp_wall.width
        height = self.bp_floor.height
        floor_fill = cq.Workplane("XY").box(length,width,height)
        self.floor_fill = floor_fill
            
    def make(self):
        super().make()
        self.make_outline()
        self.make_wall()
        self.make_floor()
        self.make_floor_fill()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bp_wall:
            wall = self.bp_wall.build()
            
            y_translate = self.width/2 - self.bp_wall.width /2
            z_translate = self.bp_wall.height/2 + self.bp_floor.height
            part = part.union(wall.translate((0,y_translate,z_translate)))
            
        if self.bp_floor:
            floor = self.bp_floor.build()
            
            y_translate = self.bp_wall.width/2
            z_translate = self.bp_floor.height /2
            part = part.union(floor.translate((0,-y_translate,z_translate)))
        
        if self.floor_fill:
            y_translate = self.width/2 - self.bp_wall.width/2
            z_translate = self.bp_floor.height/2
            part = part.union(self.floor_fill.translate((0,y_translate,z_translate)))
        return part
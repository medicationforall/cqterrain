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
import math
from cadqueryhelper import Base
from .. import tile

class TileFloor(Base):
    def __init__(self):
        super().__init__()

        #parameters
        self.length:float = 100
        self.width:float = 50
        self.height:float = 4
        
        self.tile_length:float = 15
        self.tile_width:float = 15
        self.tile_method:Callable[[float,float,float],cq.Workplane] = tile.bolt_panel
        self.count_overflow:tuple[int,int] = (0,0)
        self.tile_spacing:tuple[float,float] = (0,0)
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.tiles:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline.translate((0,0,self.height/2))
        
    def make_tile(self):
        length = self.tile_length - self.tile_spacing[0]
        width = self.tile_width - self.tile_spacing[1]
        height = self.height
        
        self.tile = self.tile_method(
            length, 
            width, 
            height
        )
    
    def make_tiles(self):
        def add_tile(loc: cq.Location) -> cq.Shape:
            return self.tile.val().located(loc) #type: ignore
        
        x_count = math.floor(self.length/self.tile_length)+self.count_overflow[0]
        y_count = math.floor(self.width/self.tile_width)+self.count_overflow[1]

        self.tiles = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = self.tile_length, 
                ySpacing = self.tile_width,
                xCount = x_count, 
                yCount= y_count, 
                center = True)
            .eachpoint(add_tile)
        )
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_tile()
        self.make_tiles()
        
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
            
        if self.tiles:
            part = (
                part
                .union(self.tiles.translate((0,0,0)))
                .intersect(self.outline.translate((0,0,0)))
            )
        
        return part.translate((0,0,self.height/2))
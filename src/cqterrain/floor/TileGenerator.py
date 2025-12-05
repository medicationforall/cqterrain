# Copyright 2025 James Adams
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
from typing import Callable
import math

def make_basic_tile(
    length:float, 
    width:float, 
    height:float
) -> cq.Workplane:
    tile = cq.Workplane("XY").box(
        length, 
        width, 
        height
    )
    return tile

class TileGenerator(Base):
    def __init__(self):
        super().__init__()
        # properties
        self.length:float = 100
        self.width:float = 100
        self.tile_length:float = 10
        self.tile_width:float = 10
        self.tile_height:float = 3
        self.tile_padding:float = 1
        self.overflow:float = 12

        self.make_tile_method:Callable[[float, float, float], cq.Workplane] = make_basic_tile
        self.call_per_tile:bool = False

        self.render_intersect:bool = True

        # shapes 
        self.tiles:cq.Workplane|None = None
        self.outline:cq.Workplane|None = None

    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.tile_height
        )
        
        self.outline = outline

    def _make_floor(self):
        if not self.make_tile_method:
            raise Exception("Missing make_tile_method callback")
        else:
            tile = self.make_tile_method(self.tile_length, self.tile_width, self.tile_height)
        
        tile_length = self.tile_length + self.tile_padding * 2
        tile_width = self.tile_width + self.tile_padding * 2
        
        x_count = math.floor((self.length+self.overflow) / tile_length)
        y_count = math.floor((self.width+self.overflow) / tile_width)

        if x_count == 0:
            raise Exception(f'x_count is zero')
            
        if y_count == 0:
            raise Exception(f'y_count is zero')

        def add_tile(loc:cq.Location) -> cq.Shape:
            l_tile = tile
            if self.call_per_tile:
                l_tile = self.make_tile_method(self.tile_length, self.tile_width, self.tile_height)
            return l_tile.val().located(loc) #type: ignore
        
        result = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = tile_length, 
                ySpacing = tile_width,
                xCount = x_count, 
                yCount= y_count, 
                center = True)
            .eachpoint(add_tile)
        )

        intersect_box = cq.Workplane("XY").box(self.length, self.width, self.tile_height)

        if self.render_intersect:
            self.tiles = result.intersect(intersect_box)
        else:
            self.tiles = result

    def make(self, parent=None):
        super().make(parent)
        self.make_outline()
        self._make_floor()

    def build_outline(self):
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part.add(self.outline)
        
        return part

    def build(self) -> cq.Workplane:
        super().build()
        if self.tiles:
            return self.tiles
        else:
            return cq.Workplane("XY")
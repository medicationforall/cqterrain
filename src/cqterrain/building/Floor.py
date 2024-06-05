# Copyright 2022 James Adams
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
from cadqueryhelper import shape, grid, Base
from typing import Callable


class Floor(Base):
    def __init__(
            self, 
            length:float = 100, 
            width:float = 100, 
            height:float = 3, 
            tile:cq.Workplane|None = None, 
            tile_padding:float = 0
        ):
        # parameters
        self.length:float = length
        self.width:float = width
        self.height:float = height
        self.tile:cq.Workplane|None = tile
        self.tile_padding:float = tile_padding

        # parts
        self.floor:cq.Workplane|None = None
        self.tile_grid:cq.Workplane|None = None
        self.grid_height:float|None = None
        self.operations:list[Callable[[cq.Workplane], cq.Workplane]] = []

    def add_operation(self, funct):
        #print('add_operation')
        self.operations.append(funct)


    def make(self):
        self.floor = cq.Workplane("XY").box(self.length, self.width, self.height)

        self.tile_grid, self.grid_height = self.__make_tile_grid()

        if self.operations and len(self.operations) > 0:
            for op in self.operations:
                self.floor = op(self.floor)


    def __make_tile_grid(self):
        if self.tile:
            bounds = self.tile.val().BoundingBox() #type: ignore
            t_width = bounds.ylen
            t_length = bounds.xlen
            t_height = bounds.zlen
            columns = math.floor(self.width/(t_width + self.tile_padding))
            rows = math.floor(self.length/(t_length + self.tile_padding))
            tile_grid = grid.make_grid(part=self.tile, dim = [t_width + self.tile_padding, t_length + self.tile_padding], columns = columns, rows = rows)
            #inside_grid = inside_grid.rotate((1, 0, 0), (0, 0, 0), -90)
            return tile_grid, t_height
        else:
            return None, None

    def build(self):
        floor_assembly = cq.Assembly()
        if self.tile_grid and self.grid_height:
            #print('add tile ggrid')
            floor_assembly.add(self.tile_grid, name="tiles", loc=cq.Location(cq.Vector(0, 0, (self.grid_height/2) + (self.height/2))))
        floor_assembly.add(self.floor, name="floor")
        comp_floor = floor_assembly.toCompound()

        #meta = {'type':'floor', 'height':tile_height + height, 'length':length, 'width':width}
        #comp_floor.metadata = meta

        #return comp_floor
        scene = cq.Workplane("XY").add(comp_floor)
        return scene
    
    def build_assembly(self):
        floor_assembly = cq.Assembly()
        if self.tile_grid and self.grid_height:
            #print('add tile ggrid')
            floor_assembly.add(self.tile_grid, name="tiles", loc=cq.Location(cq.Vector(0, 0, (self.grid_height/2) + (self.height/2))))
        floor_assembly.add(self.floor, name="floor")
        return floor_assembly.add(self.floor, name="floor")


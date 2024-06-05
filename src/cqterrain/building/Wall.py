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
from cadqueryhelper import grid, Base
import math

class Wall(Base):
    def __init__(self, 
                 length:float = 100, 
                 width:float = 3, 
                 height:float = 50, 
                 inside_tile:cq.Workplane|None = None, 
                 outside_tile:cq.Workplane|None = None
        ):

        # parameters
        self.length:float = length
        self.width:float = width
        self.height:float = height
        self.inside_tile:cq.Workplane|None = inside_tile
        self.outside_tile:cq.Workplane|None = outside_tile

        #parts
        self.wall:cq.Workplane|None = None
        self.inside_grid:cq.Workplane|None = None
        self.outside_grid:cq.Workplane|None = None

    def make(self):
        self.wall = cq.Workplane("XY").box(self.length, self.width, self.height)
        self.inside_grid = self.__make_inside_tile_grid()
        self.outside_grid = self.__make_outside_tile_grid()
        
    def _calculate_bounds(self, shape):
        if shape:
            bounds = shape.val().BoundingBox()
            length = bounds.xlen
            width = bounds.ylen
            height = bounds.zlen
            return (length, width, height)
        else:
            raise Exception('Could not resolve shape')


    def __make_inside_tile_grid(self) -> cq.Workplane|None:
        if self.inside_tile:
            length, width, height = self._calculate_bounds(self.inside_tile)

            inside_columns = math.floor(self.height/width)
            inside_rows = math.floor(self.length/length)
            inside_grid = grid.make_grid(part=self.inside_tile, dim = [width, length], columns = inside_columns, rows = inside_rows)
            inside_grid = inside_grid.rotate((1, 0, 0), (0, 0, 0), -90)
            return inside_grid
        else:
            return None

    def __make_outside_tile_grid(self)-> cq.Workplane|None:
        if self.outside_tile:
            length, width, height = self._calculate_bounds(self.outside_tile)
            outside_columns = math.floor(self.height/width)
            outside_rows = math.floor(self.length/length)
            outside_grid = grid.make_grid(part=self.outside_tile, dim = [width, length], columns = outside_columns, rows = outside_rows)
            outside_grid = outside_grid.rotate((1, 0, 0), (0, 0, 0), -90)
            return outside_grid
        else:
            return None
        

    def build(self):
        scene = (
            cq.Workplane("XY")
            .union(self.wall)
        )

        if self.inside_grid:
            length, width, height = self._calculate_bounds(self.inside_tile)
            scene = scene.add(self.inside_grid.translate((0, -1*(self.width/2+height/2), 0)))

        if self.outside_grid:
            length, width, height = self._calculate_bounds(self.outside_tile)
            scene = scene.add(self.outside_grid.translate((0, (self.width/2+height/2), 0)))

        return scene

    def build_assembly(self):
        wall_assembly = cq.Assembly()
        wall_assembly.add(self.wall, name="wall")

        if self.inside_grid:
            length, width, height = self._calculate_bounds(self.inside_tile)
            wall_assembly.add(
                self.inside_grid, 
                name="insideGrid", 
                loc=cq.Location(cq.Vector(0, -1*(self.width/2+height/2), 0)))

        if self.outside_grid:
            length, width, height = self._calculate_bounds(self.outside_tile)
            wall_assembly.add(
                self.outside_grid, 
                name="outsideGrid", 
                loc=cq.Location(cq.Vector(0, (self.width/2+height/2), 0)))

        return wall_assembly

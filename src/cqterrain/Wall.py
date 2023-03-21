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
from cadqueryhelper import shape
from cadqueryhelper import grid
import math

class Wall:
    def __init__(self, length = 100, width = 3, height = 50, inside_tile=None, outside_tile=None):
        self.length = length
        self.width = width
        self.height = height
        self.inside_tile = inside_tile
        self.outside_tile = outside_tile

        #make
        self.wall = None
        self.inside_grid = None
        self.outside_grid  = None
        self.inside_height = None
        self.outside_height = None

    def make(self):
        self.wall = shape.cube(self.length, self.width, self.height)
        self.inside_grid, self.inside_height = self.__make_inside_tile_grid()
        self.outside_grid, self.outside_height = self.__make_outside_tile_grid()

    def __make_inside_tile_grid(self):
        if self.inside_tile:
            bounds = self.inside_tile.val().BoundingBox()
            inside_width = bounds.ylen
            inside_length = bounds.xlen
            inside_height = bounds.zlen
            inside_columns = math.floor(self.height/inside_width)
            inside_rows = math.floor(self.length/inside_length)
            inside_grid = grid.make_grid(part=self.inside_tile, dim = [inside_width, inside_length], columns = inside_columns, rows = inside_rows)
            inside_grid = inside_grid.rotate((1, 0, 0), (0, 0, 0), -90)
            return inside_grid, inside_height
        else:
            return None, None

    def __make_outside_tile_grid(self):
        if self.outside_tile:
            bounds = self.outside_tile.val().BoundingBox()
            outside_width = bounds.ylen
            outside_length = bounds.xlen
            outside_height = bounds.zlen
            outside_columns = math.floor(self.height/outside_width)
            outside_rows = math.floor(self.length/outside_length)
            outside_grid = grid.make_grid(part=self.outside_tile, dim = [outside_width, outside_length], columns = outside_columns, rows = outside_rows)
            outside_grid = outside_grid.rotate((1, 0, 0), (0, 0, 0), -90)
            return outside_grid, outside_height
        else:
            return None, None

    def build(self):
        wall_assembly = cq.Assembly()
        wall_assembly.add(self.wall, name="wall")

        if self.inside_grid:
            wall_assembly.add(self.inside_grid, name="insideGrid" , loc=cq.Location(cq.Vector(0, -1*(self.width/2+self.inside_height/2), 0)))

        if self.outside_grid:
            wall_assembly.add(self.outside_grid, name="outsideGrid" , loc=cq.Location(cq.Vector(0, (self.width/2+self.inside_height/2), 0)))

        comp_wall = wall_assembly.toCompound()
        scene = cq.Workplane("XY").add(comp_wall)
        return scene

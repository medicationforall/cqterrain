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

class Floor():
    def __init__(self, length=100, width=100, height=3, tile=None, tile_padding=0):
        self.length = length
        self.width = width
        self.height = height
        self.tile = tile
        self.tile_padding = tile_padding

        self.floor = None
        self.tile_grid = None
        self.grid_height = None

    def make(self):
        self.floor = shape.cube(self.length, self.width, self.height)
        self.tile_grid, self.grid_height = self.__make_tile_grid()

    def __make_tile_grid(self):
        if self.tile:
            bounds = self.tile.val().BoundingBox()
            t_width = bounds.ylen
            t_length = bounds.xlen
            t_height = bounds.zlen
            columns = math.floor(self.width/t_width)
            rows = math.floor(self.length/t_length)
            tile_grid = grid.make_grid(part=self.tile, dim = [t_width + self.tile_padding, t_length + self.tile_padding], columns = columns, rows = rows)
            #inside_grid = inside_grid.rotate((1, 0, 0), (0, 0, 0), -90)
            return tile_grid, t_height
        else:
            return None, None

    def build(self):
        floor_assembly = cq.Assembly()
        if self.tile_grid:
            #print('add tile ggrid')
            floor_assembly.add(self.tile_grid, name="tiles", loc=cq.Location(cq.Vector(0, 0, (self.grid_height/2) + (self.height/2))))
        floor_assembly.add(self.floor, name="floor")
        comp_floor = floor_assembly.toCompound()

        #meta = {'type':'floor', 'height':tile_height + height, 'length':length, 'width':width}
        #comp_floor.metadata = meta

        #return comp_floor
        scene = cq.Workplane("XY").add(comp_floor)
        return scene

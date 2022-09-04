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

def wall(length = 100, width = 3, height = 50):
    return shape.cube(length, width, height)

def tile_wall(inside_tile=None, outside_tile=None, length = 100, width = 3, height = 50):
    wall_part = wall(length = length, width = width, height = height)

    wall_assembly = cq.Assembly()
    wall_assembly.add(wall_part, name="wall")

    if inside_tile:
        print('found inside tile')
        inside_meta = __resolve_tile_meta(inside_tile)
        inside_width = inside_meta['width']
        inside_length = inside_meta['length']
        inside_height = inside_meta['height']
        inside_columns = math.floor(height/inside_width)
        inside_rows = math.floor(length/inside_length)

        print('inside tile meta', inside_meta, inside_columns, inside_rows)
        inside_grid = grid.make_grid(part=inside_tile, dim = [inside_width, inside_length], columns = inside_columns, rows = inside_rows)
        inside_grid = inside_grid.rotate((1, 0, 0), (0, 0, 0), -90)

        wall_assembly.add(inside_grid, name="insideGrid" , loc=cq.Location(cq.Vector(0, -(width/2+inside_height/2), 0)))

    if outside_tile:
        print('found outside tile')
        outside_meta = __resolve_tile_meta(outside_tile)
        outside_width = outside_meta['width']
        outside_length = outside_meta['length']
        outside_height = outside_meta['height']
        outside_columns = math.floor(height/outside_width)
        outside_rows = math.floor(length/outside_length)

        print('outside tile meta', outside_meta, outside_columns, outside_rows)
        outside_grid = grid.make_grid(part=outside_tile, dim = [outside_width, outside_length], columns = outside_columns, rows = outside_rows)
        outside_grid = outside_grid.rotate((1, 0, 0), (0, 0, 0), -90)

        wall_assembly.add(outside_grid, name="outsideGrid" , loc=cq.Location(cq.Vector(0, (width/2+outside_height/2), 0)))

    comp_wall = wall_assembly.toCompound()

    meta = {'type':'wall', 'height':height, 'length':length, 'width':width}
    comp_wall.metadata = meta

    return comp_wall

def __resolve_tile_meta(tile):
    meta = None
    tile_attributes = dir(tile)
    if 'metadata' in tile_attributes:
        meta = tile.metadata
    return meta

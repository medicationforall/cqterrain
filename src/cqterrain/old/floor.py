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

def floor(length=100, width=100, height=3):
    work = shape.cube(length, width, height)
    meta = {'type':'floor', 'height':height , 'length':length, 'width':width}
    work.metadata = meta
    return work

def make_tile_floor(tile, length=100, width=100, height=3):
    tile_width = 5
    tile_length = 5
    tile_height = 5

    tile_meta = __resolve_tile_meta(tile)

    if tile_meta and 'width' in tile_meta and 'length' in tile_meta:
        tile_width = tile_meta['width']
        tile_length = tile_meta['length']
        tile_height = tile_meta['height']
    else:
        raise Exception('Could not resolve width and or length from tile metadata', tile_meta)

    columns = math.floor(width/tile_width)
    rows = math.floor(length/tile_length)

    tile_grid = grid.make_grid(part=tile, dim = [tile_width, tile_length], columns = columns, rows = rows)
    floor_part = make_floor(length, width, height)

    floor_assembly = cq.Assembly()
    floor_assembly.add(tile_grid, name="tiles", loc=cq.Location(cq.Vector(0, 0, (tile_height/2) + (height/2))))
    floor_assembly.add(floor_part, name="floor")
    comp_floor = floor_assembly.toCompound()

    meta = {'type':'floor', 'height':tile_height + height, 'length':length, 'width':width}
    comp_floor.metadata = meta

    return comp_floor

def __resolve_tile_meta(tile):
    meta = None
    tile_attributes = dir(tile)
    if 'metadata' in tile_attributes:
        meta = tile.metadata
    return meta

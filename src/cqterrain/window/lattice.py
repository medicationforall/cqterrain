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
from cadqueryhelper.grid import grid
import math

def lattice(
        length:float = 20, 
        height:float = 40,  
        tile_size:float = 4, 
        lattice_width:float = 1, 
        lattice_height:float = 1, 
        lattice_angle:float = 45
    ) -> cq.Workplane:
    # Determine longest distance between points
    hyp = math.hypot(length, height)
    columns= math.floor(hyp / (tile_size+lattice_width))
    rows= math.floor(hyp / (tile_size+lattice_width))

    # Make a flat plane
    pane = cq.Workplane("XY").box(length, lattice_height, height)

    #make the cutout tile
    tile = cq.Workplane("XY").box(tile_size, lattice_height, tile_size).rotate((1,0,0),(0,0,0),90)
    tiles = grid.make_grid(tile, [tile_size+lattice_width, tile_size+lattice_width], rows=columns, columns=rows).rotate((1,0,0),(0,0,0),-90).rotate((0,1,0),(0,0,0),lattice_angle)
    combine = pane.cut(tiles)
    return combine
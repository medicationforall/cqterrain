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
import math
from cadqueryhelper import grid

def tiles_alt(
        tile:cq.Workplane, 
        face:cq.Workplane,
        length:float, 
        width:float,
        height:float, 
        t_length:float, 
        t_width:float, 
        angle:float, 
        odd_col_push:list = [0,0], 
        debug:bool = False, 
        intersect:bool = True
    ):
    hyp = math.hypot(length, height)
    columns = math.floor(width / t_width)+2
    
    rows = math.floor(hyp/ t_length)+2
    
    #log(f'{columns=}')

    c_face = face
    plane = (
        c_face.wires()
        .toPending()
        .translate((3, 0, 0.0))
        .toPending()
        .loft()
    )

    tiles = (
        grid.make_grid(
            tile, 
            [t_length, t_width], 
            rows = rows, 
            columns = columns, 
            odd_col_push = odd_col_push
        )
        .rotate((0,1,0),(0,0,0),-angle)
        .translate(((length/2),0,0))
    )
    

    composite = (
        cq.Workplane("XY")
        .union(tiles)
    )

    if debug:
        combine = composite.union(plane)
    else:
        combine = composite.intersect(plane)

    if intersect:
        return combine
    else:
        return composite
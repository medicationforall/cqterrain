# Copyright 2024 James Adams
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
from typing import Literal

def angled_stairs( 
    height:float = 71,
    inner_diameter:float = 76,
    diameter:float = 75+45,
    stair_height:float|None = 5.461538461538462,
    stair_count:int|None = None,
    operation:Literal['chamfer', 'fillet'] = 'chamfer',
    distance:float = 1,
    debug:bool = False
) -> cq.Workplane:
    cut_cylinder = cq.Workplane("XY").cylinder(height, inner_diameter/2)
    outline = cq.Workplane("XY").cylinder(height, diameter/2)
    intersect = cq.Workplane("XY").box(diameter,diameter,height)
    
    if stair_count is None and stair_height is not None:
        stair_count = math.floor(height / stair_height)
    elif stair_count is not None:
        stair_height = height / stair_count
    else:
        raise Exception('stair_count and stair_height are None')
    
    stair_deg = 90 / stair_count
    
    #outline
    stair_outline = cq.Workplane("XY").cylinder(stair_height, diameter/2)
    stair_single = (
        cq.Workplane("XY")
        .union(stair_outline)
        .cut(cut_cylinder)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    )
    
    if distance > stair_height:
        distance = stair_height - 0.00001
    
    if operation == 'chamfer':
        stair_single = (
            stair_single
            .faces("-Y")
            .edges(">Z")
            .chamfer(distance)
        )
    elif operation == 'fillet':
        stair_single = (
            stair_single
            .faces("-Y")
            .edges(">Z")
            .fillet(distance)
        )
    
    #return stair_single
    
    stair_rough = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_cylinder)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    )
    
    stairs = cq.Workplane("XY")
    
    for i in range(stair_count):
        #log(f"add stair {i}, {stair_deg*i}")
        stairs = stairs.translate((0,0,-stair_height*1)).union(stair_single.rotate((0,0,1),(0,0,0),-stair_deg*i))
    
    if debug:
        return stairs.translate((0,0,height/2-stair_height/2)).add(stair_rough)
    else:
        return stairs.translate((0,0,height/2-stair_height/2)).intersect(stair_rough)
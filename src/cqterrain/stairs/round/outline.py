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

def outline(
    height:float = 71,
    inner_diameter:float = 76,
    diameter:float = 75+45,
    rotate:float = 40,
    debug:bool = False
):
    cut_cylinder = cq.Workplane("XY").cylinder(height, inner_diameter/2)
    outline = cq.Workplane("XY").cylinder(height, diameter/2)
    intersect = cq.Workplane("XY").box(diameter,diameter,height)
    
    stair_rough = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_cylinder)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    )
    
    if debug:
        return (
            stair_rough
            .add(stair_rough.rotate((0,0,1),(0,0,0),-rotate))
        ).translate((0,0,height/2))
    else:
        return (
            stair_rough
            .intersect(stair_rough.rotate((0,0,1),(0,0,0),-rotate))
        ).translate((0,0,height/2))
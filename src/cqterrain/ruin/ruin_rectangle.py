# Copyright 2026 James Adams
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

def ruin_rectangle(
length:float = 75, 
width:float = 50, 
height:float = 5,
points:int = 7,
adjustments:list[tuple[float,float]] = [],#[(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
debug:bool = False
):
    pts:list[tuple[float,float]] = [(0,0)]#,(0,width),(length,0)]
    
    x_step = length / (points+1)
    y_step = width / (points+1)
    
    test_cube = cq.Workplane("XY").box(1,1,1)
    test_cubes = cq.Workplane("XY")
    
    #build out your points
    for i in range(points+2):
        x_translate:float = x_step*i
        y_translate:float = width
        
        if i > 0 and i < points+1 and (i-1) < len(adjustments):
            coord = adjustments[i-1]
            x_translate += coord[0]
            y_translate += coord[1]
        
        pts.append((x_translate, y_translate))
        
        test_cubes = (
            test_cubes.add(
                test_cube
                .translate((x_translate,y_translate,0))
            )
        )
        
    pts.append((length,0))
        
    ruin = (
        cq.Workplane("XY")
        .polyline(pts)
        .close()
    )

    if height:
        ruin = ruin.extrude(height)
        
    if debug:
        ruin = ruin.add(test_cubes)
    
    return ruin
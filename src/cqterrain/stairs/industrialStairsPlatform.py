# Copyright 2023 James Adams
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

def make_step(
          i:int, 
          stair_interval:float, 
          width:float
    ) -> cq.Workplane:
    step = cq.Workplane("XY").box(
        stair_interval,
        width, 
        stair_interval*(i+1)
    )
    
    cut_out = cq.Workplane("XY").box(
        stair_interval,
        (width)-4, 
        stair_interval-2
    ).faces("Z").edges("X").chamfer(2)
    
    #return cut_out
    cut_z_translate = ((stair_interval/2)*(i))-1
    return step.cut(cut_out.translate((0,0,cut_z_translate)))

def industrial_stairs_platform(
        length:float = 75, 
        width:float = 75,
        height:float = 75,
        stair_count:int = 10,
        stair_chamfer:float|None = None
    ) -> cq.Workplane:
    stair_interval = length / stair_count
    
    stairs =(cq.Workplane("XY"))
    
    for i in range(stair_count):
        step = make_step(i, stair_interval, width)
        
        if stair_chamfer:
            step = step.faces("<Y").edges("Z").chamfer(stair_chamfer)
            
        stairs = stairs.union(
            step.translate((
                length-(stair_interval/2)-stair_interval*i,
                0,
                -1*(height/2)+(stair_interval*(i+1)/2)
            )))
    return stairs.translate((-1*(length/2),0,0))
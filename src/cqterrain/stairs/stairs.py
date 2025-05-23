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
from cadqueryhelper import series
import math


def __make_rail(
        length:float, 
        height:float, 
        run:float, 
        rail_width:float, 
        rail_height:float
    ):
    rail_length = length-run
    bookend_length = (length - rail_length) / 2
    rail = shape.rail(length = rail_length, width = rail_width, height = height, inner_height = rail_height)

    rail_assembly = cq.Assembly()
    rail_assembly.add(rail, name="r_rail", loc=cq.Location(cq.Vector(0, 0, 0)))

    if bookend_length > 0:
        #print('append rail ends')
        end = cq.Workplane("XY").box(bookend_length, rail_width, rail_height)
        rail_assembly.add(end, name="top", loc=cq.Location(cq.Vector((rail_length/2)+(bookend_length/2), 0, (height/2)-(rail_height/2))))
        rail_assembly.add(end, name="bottom", loc=cq.Location(cq.Vector(-1*((rail_length/2)+(bookend_length/2)), 0, -1*((height/2)-(rail_height/2)))))


    comp_rail = rail_assembly.toCompound()
    return comp_rail

def stairs(
        length:float = 30, 
        width:float = 10, 
        height:float = 30,  
        run:float = 5, 
        stair_length_offset:float = 0, 
        stair_height:float = 1, 
        stair_height_offset:float = 0, 
        rail_width:float = 1, 
        rail_height:float = 5, 
        step_overlap:float|None = None
    ):
    stair_repeat = math.floor(length / (run + stair_length_offset))
    rise = (height - (stair_repeat * stair_height)) / stair_repeat

    rail = __make_rail(length, height, run, rail_width, rail_height)

    if not step_overlap:
        step_overlap = rail_width/2

    step = cq.Workplane("XY").box(length = run, width = (width-(rail_width*2) + (step_overlap*2)), height = stair_height)
    steps = series(shape = step, size = stair_repeat, length_offset = stair_length_offset, height_offset = rise+stair_height_offset)

    stair_assembly = cq.Assembly()
    stair_assembly.add(rail, name="r_rail", loc=cq.Location(cq.Vector(0, -1*(rail_width/2), 0)))
    stair_assembly.add(steps, name="steps", loc=cq.Location(cq.Vector(0, -1*((width)/2), 0)))
    stair_assembly.add(rail, name="l_rail", loc=cq.Location(cq.Vector(0, -1*(width-(rail_width/2)), 0)))

    comp_stairs = stair_assembly.toCompound()

    # center shape
    comp_stairs = comp_stairs.translate((0,(width/2),0))
    return comp_stairs

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
from . import rectangle
from . import corner

def three_wall_section(
        length:float = 50, 
        width:float = 50, 
        height:float = 50, 
        wall_width:float = 5
):
    ex_base = rectangle(length=length, width = width, height = wall_width)
    ex_corner_wall_one = (
        corner(length=length, width = height, height = wall_width)
        .translate((0,0,-wall_width))
        .rotate((1,0,0),(0,0,0),-90)
    )
    
    ex_wall_two = (
        rectangle(length=width, width = height, height = wall_width).translate((0,0,0))
        .rotate((1,0,0),(0,0,0),-90)
        .rotate((0,0,1),(0,0,0),-90)
    )
    
    ex_corner_wall_three = (
        corner(length=length, width = height, height = wall_width)
        .translate((0,0,-wall_width))
        .rotate((1,0,0),(0,0,0),-90)
        .translate((0,width-wall_width,0))
    )
    
    cut_corner = (
        corner(length=length, width = height, height = width)
        .translate((0,0,-width))
        .rotate((1,0,0),(0,0,0),-90)
    )
    
    cut_struts = (
        cq.Workplane("XY")
        .union(ex_base)
        .union(ex_wall_two)
        .cut(cut_corner)
    )

    ruin = (
        cq.Workplane("XY")
        .union(ex_base)
        .union(ex_corner_wall_one)
        .union(ex_wall_two)
        .union(ex_corner_wall_three)
    )
    
    corner_combined = ruin.cut(cut_struts)
    #return cut_struts
    return corner_combined
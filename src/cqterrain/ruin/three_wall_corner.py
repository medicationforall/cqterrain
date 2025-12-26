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
from . import corner

def three_wall_corner(
        length:float = 50, 
        width:float = 50, 
        height:float = 50, 
        wall_width:float = 5
):
    ex_base = corner(length=length, width = width, height = wall_width)
    ex_wall_one = (
        corner(length=length, width = height, height = wall_width)
        .translate((0,0,-wall_width))
        .rotate((1,0,0),(0,0,0),-90)
    )
    
    ex_wall_two = (
        corner(length=width, width = height, height = wall_width).translate((0,0,0))
        .rotate((1,0,0),(0,0,0),-90)
        .rotate((0,0,1),(0,0,0),-90)
    )
    
    strut_one = cq.Workplane("XY").add(ex_base).intersect(ex_wall_one)
    strut_two = cq.Workplane("XY").add(ex_base).intersect(ex_wall_two)
    strut_three = cq.Workplane("XY").add(ex_wall_one).intersect(ex_wall_two)
    
    struts = (
        cq.Workplane("XY").union(strut_one).union(strut_two)
        .union(strut_three))
    
    c_strut_one = cq.Workplane("XY").box(length,wall_width,wall_width)
    c_strut_two = cq.Workplane("XY").box(width,wall_width,wall_width)
    c_strut_three = cq.Workplane("XY").box(height,wall_width,wall_width)
    
    cut_corners = (
        cq.Workplane("XY")
        .union(
            c_strut_one
            .translate((length/2,wall_width/2,wall_width/2))
        )
        .union(
            c_strut_two
            .translate((width/2,-wall_width/2,wall_width/2))
            .rotate((0,0,1),(0,0,0),-90)
        )
        .union(
            c_strut_three
            .translate((height/2,wall_width/2,-wall_width/2))
            .rotate((0,1,0),(0,0,0),90)
        )
        .cut(struts)
    )
    
    ruin = (
        cq.Workplane("XY")
        .union(ex_base)
        .union(ex_wall_one)
        .union(ex_wall_two)
    )
    
    corner_combined = ruin.cut(cut_corners)
    return corner_combined
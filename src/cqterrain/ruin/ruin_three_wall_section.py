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
from . import ruin_rectangle, ruin_corner, corner

def ruin_three_wall_section(
    length:float = 50, 
    width:float = 50, 
    height:float = 50, 
    wall_width:float = 5,
    base_points:int = 5,
    base_adjustments:list[tuple[float,float]] = [(10,-5),(-2,-2),(3,5),(-10,-10),(0,3)],
    x_points:int = 3,
    x_adjustments:list[tuple[float,float]] = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
    x_points_two:int = 4,
    x_adjustments_two:list[tuple[float,float]] = [(10,-5),(-2,-2),(3,5),(-5,-3),(0,3)],
    y_points:int = 4,
    y_adjustments:list[tuple[float,float]] = [(10,-20),(-2,-2),(3,5),(-10,-7),(0,3)],
    debug:bool = False
):
    ex_base = ruin_rectangle(
        length= width, 
        width = length, 
        height = wall_width,
        points = base_points,
        adjustments = base_adjustments,
        debug = debug
    ).rotate((0,0,1),(0,0,0),90).translate((0,width,0))
    
    ex_corner_wall_one = (
        ruin_corner(
            length=length, 
            width = height, 
            height = wall_width,
            points = x_points,
            adjustments = x_adjustments,
            debug = debug
        )
        .translate((0,0,-wall_width))
        .rotate((1,0,0),(0,0,0),-90)
    )
    
    ex_wall_two = (
        ruin_rectangle(
            length=width, 
            width = height, 
            height = wall_width,
            points = y_points,
            adjustments = y_adjustments,
            debug = debug
        ).translate((0,0,0))
        .rotate((1,0,0),(0,0,0),-90)
        .rotate((0,0,1),(0,0,0),-90)
    )
    
    ex_corner_wall_three = (
        ruin_corner(
            length=length, 
            width = height, 
            height = wall_width,
            points = x_points_two,
            adjustments = x_adjustments_two,
            debug = debug
        )
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

    #return ex_wall_two
    return corner_combined
    #return ruin
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

import cadquery as cq

def _make_line(
        length, 
        width, 
        line_width, 
        line_depth,
        x_divisor,
        y_divisor
):
    pts = [
        (0,0),
        (0,width/y_divisor),
        (length/x_divisor+line_width/2,width/y_divisor+width/y_divisor),
        (length/x_divisor+line_width/2,width/y_divisor+width/y_divisor-line_width),
        (line_width,width/y_divisor-line_width/2),
        (line_width,0),
    ]

    cut_line = (
        cq.Workplane("XY")
        .polyline(pts)
        .close()
        .extrude(line_depth)
    ).translate((-1*(line_width/2),0,-1*(line_depth/2)))
    return cut_line

def carton2(
    length = 30, 
    width = 25, 
    height = 4, 
    line_width = 2, 
    line_depth = 1.5,
    x_divisor = 2,
    y_divisor = 3
):
    cut_line = _make_line(
        length, 
        width, 
        line_width, 
        height,
        x_divisor,
        y_divisor
    )
    
    outline = cq.Workplane("XY").box(length, width, height)
    outline_2 = cq.Workplane("XY").box(length-line_depth*2, width-line_depth*2, height-line_depth)
    cut_end = cq.Workplane("XY").box(line_depth,line_width,height)

    cut_lines_combined = (
        cq.Workplane("XY")
        .union(cut_line.translate((0,-1*(width/2),0)))
        .union(cut_line.translate((0,-1*(width/2),0)).rotate((0,0,1),(0,0,0),180))
        .cut(outline_2.translate((0,0,-1*line_depth/2)))
    )
    
    carton2_tile = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_lines_combined)
    )
    return carton2_tile
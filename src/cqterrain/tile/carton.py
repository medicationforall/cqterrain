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

def _carton_line(
    length:float = 30, 
    width:float = 25, 
    line_width:float = 2,
    line_depth:float = 1,
    x_divisor:float = 3,
    y_divisor:float = 2
) -> cq.Workplane:
    pts = [
        (0,0),
        (0,line_width),
        (length/x_divisor-line_width/2,line_width),
        (length/x_divisor+length/x_divisor,width/y_divisor), 
        (length,width/y_divisor),
        (length,width/y_divisor-line_width),
        (length/x_divisor+length/x_divisor+line_width/2,width/y_divisor-line_width),
        (length/x_divisor,line_width-line_width),
    ]
    
    cut_line = (
        cq.Workplane("XY")
        .polyline(pts)
        .close()
        .extrude(line_depth)
    ).translate((-1*(length/2),-1*(width/(y_divisor*2)),-1*(line_depth/2)))
    return cut_line

def carton(
        length:float = 30, 
        width:float = 25, 
        height:float = 4,
        line_width:float = 2,
        line_depth:float = 1,
        x_divisor:float = 3,
        y_divisor:float = 3
) -> cq.Workplane:
    cut_line = _carton_line(
        length, 
        width, 
        line_width, 
        line_depth, 
        x_divisor,
        y_divisor
    )
    outline = cq.Workplane("XY").box(length, width, height)    
    cut_end = cq.Workplane("XY").box(line_depth,line_width,height)
    
    carton_tile = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_line.translate((0,0,height/2 - line_depth/2)))
        .cut(cut_end.translate((length/2-line_depth/2,width/(y_divisor*2)-line_width/2,0)))
        .cut(cut_end.translate((-1*(length/2-line_depth/2),-1*(width/(y_divisor*2)-line_width/2),0)))
    )
    return carton_tile
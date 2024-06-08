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

def _make_lines(
    length:float, 
    width:float, 
    height:float,
    line_width:float
) -> cq.Workplane:
    outline = cq.Workplane("XY").box(length, width, height)
    hyp = math.hypot(length, width)
    #log(hyp)
    
    angle = length/hyp
    angle_radians = math.acos((angle))
    angle_deg = math.degrees(angle_radians)
    #log(angle_deg)
    
    line = (
        cq.Workplane("XY")
        .box(hyp, line_width, height)
        
    )
    
    lines = (
        cq.Workplane("XY")
        .union(line.rotate((0,0,1),(0,0,0),angle_deg))
        .union(line.rotate((0,0,1),(0,0,0),-1*angle_deg))
    )
    return lines

def charge(
    length:float = 30, 
    width:float = 25, 
    height:float = 4,
    line_width:float = 3,
    line_depth:float = 1,
    corner_chamfer:float = 4,
    edge_chamfer:float = 2,
    padding:float = 2.5
) -> cq.Workplane:
    outline = cq.Workplane("XY").box(
        length, 
        width, 
        height
    )
    
    if corner_chamfer:
        outline = (
            outline
            .faces("X or -X")
            .edges("Z")
            .chamfer(corner_chamfer)
        )
        
    if edge_chamfer:
        outline = (
            outline
            .faces("Z")
            .chamfer(edge_chamfer)
        )
        
    lines = _make_lines(
        length-(edge_chamfer*2)-padding*2, 
        width-(edge_chamfer*2)-padding*2,
        line_depth,
        line_width, 
        
    )
    
    charge_tile = (
        cq.Workplane("XY")
        .union(outline)
        .cut(lines.translate((0,0,height/2-line_depth/2)))
    )
    
    return charge_tile
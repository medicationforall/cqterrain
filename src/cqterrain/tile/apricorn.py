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

def _make_lines(
    length:float, 
    height:float,
    line_width:float,
    center_radius:float
) -> cq.Workplane:
    line = cq.Workplane("XY").box(length, line_width, height)
    center = cq.Workplane("XY").cylinder(height, center_radius+line_width)
    cut_center = cq.Workplane("XY").cylinder(height, center_radius)
    return center.union(line).cut(cut_center)

def apricorn(
    length:float = 30, 
    width:float = 25, 
    height:float = 4,
    line_width:float = 2,
    line_depth:float = .5,
    center_radius:float|None = None,
    width_radius_divisor:float = 4
) -> cq.Workplane:
    if not center_radius:
        center_radius = width / width_radius_divisor
    
    lines = _make_lines(
        length, 
        height,
        line_width,
        center_radius
    )
    
    cut_lines = _make_lines(
        length - line_depth*2,
        height - line_depth,
        line_width,
        center_radius
    ).translate((0,0,-1*(line_depth/2)))
    
    combined_lines = lines.cut(cut_lines)

    outline = cq.Workplane("XY").box(length, width, height)
    
    apricorn_tile = (
        cq.Workplane("XY")
        .union(outline)
        .cut(combined_lines)
    )
    return apricorn_tile
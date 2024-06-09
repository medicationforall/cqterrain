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

def truchet_triangle(
    length:float = 10, 
    width:float = 10, 
    height:float = 4, 
    min_height:float = 2
) -> cq.Workplane:
    
    base = cq.Workplane("XY").box(length, width, min_height).translate((0,0,-(min_height/2)))
    pts = [(0,0),(length,0),(length,width)]
    triangle = (cq.Workplane("XY").center(-length/2,-width/2).polyline(pts).close().extrude(height-min_height))
    
    return base.union(triangle).translate((0,0,min_height)).translate((0,0,-(height/2)))


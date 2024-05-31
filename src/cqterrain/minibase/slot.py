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
from . import make_magnet_outline

def slot(
        length:float = 24, 
        width:float = 50, 
        height:float = 3, 
        taper:float = -1, 
        render_magnet:bool = True,
        magnet_diameter:float = 3, 
        magnet_height:float = 2
    ) -> cq.Workplane:
    base = (
        cq.Workplane("XY" )
        .slot2D(width, length, 90)
        .workplane(offset=height)
        .slot2D(width+taper, length+taper, 90)
        .loft(combine=True)
        .translate((0,0,-1*(height/2)))
    )
    h_solid = make_magnet_outline(height, magnet_diameter,  magnet_height)

    minibase = cq.Workplane("XY").add(base)
    if render_magnet:
        minibase = minibase.cut(h_solid)
    return minibase
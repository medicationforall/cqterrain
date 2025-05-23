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
from . import slot
from ..damage import uneven_plane

def slot_uneven(
        length:float = 75,
        width:float = 30,
        base_height:float = 3,
        taper:float = -1,
        render_magnet:bool = True,  
        magnet_diameter:float = 3, 
        magnet_height:float = 2,
        detail_height:float = 3,
        uneven_height:float = 4,
        peak_count:tuple[int,int]|int = (9,10),
        segments:int = 6,
        seed:str = "seed"
    ) -> cq.Workplane:
    # slot base
    mini_base = slot(
        length = width, 
        width = length, 
        height = base_height, 
        taper = taper,
        render_magnet = render_magnet,  
        magnet_diameter = magnet_diameter, 
        magnet_height = magnet_height
    ).rotate((0,0,1),(0,0,0),90)

    top = (
           mini_base
           .faces("Z")
           .wires()
           .toPending()
           .extrude(detail_height)
           )
    
    # uneven plane
    u_plane_safe = uneven_plane(
        length = length, 
        width = width,
        height = uneven_height,
        peak_count = peak_count,
        segments = segments,
        seed = seed,
        render_plate = True,
        plate_height = 0.1
    )
        
    u_plane_safe = u_plane_safe.translate((0,0,base_height/2 + uneven_height/2))

    scene = (
        cq.Workplane("XY")
        .union(top)
        .intersect(u_plane_safe)
        .add(mini_base)
    )
    
    return scene
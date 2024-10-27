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
import random
from cadqueryhelper.wave import uneven 
from typing import List

def uneven_plane(
    length:float = 10, 
    width:float = 50,
    segments:int = 5,
    height:float = 2.5,
    min_height:float = 0.0001,
    step:float = .5,
    peak_count:tuple[int,int]|int = (4,5), 
    seed:str|None = None,
    render_plate:bool = True,
    plate_height:float = 0.28
):
    axis:str = "XZ"
    segment_width:float = width / segments
    faces:List[cq.Workplane] = []
    
    u_plane:cq.Workplane = cq.Workplane("XY")
    
    if seed:
        random.seed(seed)
        
    #make faces
    for i in range(segments+1):
        face = uneven(
            length=length,
            width=height,
            min_width=min_height,
            step=step,
            count = peak_count,
            axis = axis,
            seed = None,
            offset = i* segment_width
        )
        faces.append(face)
    
    #make segments
    for i in range(segments):
        uneven_segment = (
            cq.Workplane(axis)
            .add(faces[i])
            .add(faces[i+1])
            .wire().toPending()
            .loft(combine=True)
        )
        
        u_plane = u_plane.union(uneven_segment)
        
    u_plane = u_plane.translate((0,width/2,0))
    if render_plate:
        base_plate = cq.Workplane("XY").box(length, width, plate_height)
        u_plane = u_plane.union(base_plate.translate((0,0,-(height/2-plate_height/2))))

    return u_plane
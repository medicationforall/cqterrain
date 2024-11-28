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
from . import pipe_face

def connector(
        length:float = 2, 
        radius:float = 11.5, 
        face_height:float = 23
    ) -> cq.Workplane:
    outline = (
        pipe_face()
        .extrude(length)
        .translate((0,0,-1*(length/2)))
        .rotate((0,1,0),(0,0,0),90)
        .translate((0,0,face_height/2))
    )

    connector_plate = (
        cq.Workplane("XY")
        .cylinder(length, radius)
        .rotate((0,1,0),(0,0,0),90)
        .translate((0,0,radius+.5))
    )
    
    combined = (
        connector_plate
        .union(outline)
        .translate((0,0,-1*(radius+.5)))
    )
    #return outline
    return combined
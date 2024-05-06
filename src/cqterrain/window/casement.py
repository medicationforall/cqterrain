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
from . import frame, grill

def casement(
        length:float = 20, 
        width:float = 4, 
        height:float = 40, 
        colums:int = 2, 
        rows:int = 3, 
        frame_width:float = 2, 
        grill_width:float = 1, 
        grill_height:float = 1
    ) -> cq.Workplane:
    outline = cq.Workplane("XY").box(length, width, height)
    window = frame(length, width, height, frame_width)
    w_grill = grill(length, height, colums, rows, grill_width, grill_height)
    return window.add(w_grill)
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
from . import cinquefoil

def cinquefoil_frame(
        outer_radius:float = 7.5, 
        radius:float = 5, 
        sides:int = 5, 
        inner_radius:float = 3, 
        height:float = 2
    ) -> cq.Workplane:
    circles = cinquefoil(radius, sides, inner_radius, height)
    frame_circle = cq.Workplane("XY").cylinder(height, outer_radius)
    result = cq.Workplane("XY").add(frame_circle).cut(circles)
    return result
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

def hip(
        length:float = 40, 
        width:float = 40, 
        top:float = 0, 
        left:float = 0, 
        right:float = 0, 
        height:float = 40
    ) -> cq.Workplane:
    top_r = top / 2
    max_w = width / 2
    max_l = length / 2

    roof = (
        cq.Workplane("XY")
        .wedge(
            length,
            height,
            width,
            max_l - top_r - left,
            max_w - top_r,
            max_l + top_r + right,
            max_w + top_r
        )
        .rotate((1,0,0), (0,0,0), -90)
    )
    return roof
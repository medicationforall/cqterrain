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
from .. import pipe as terrain_pipe

def pipe(
        length:float = 25, 
        width:float = 25, 
        height:float = 4,

        radius:float = 4,
        inner_radius:float = 3,
        segment_length:float = 6,
        space:float = 4
    ) -> cq.Workplane:

    outline = cq.Workplane("XY").box(length, width, height)

    tile_pipe = terrain_pipe.corrugated_straight(
        length, 
        radius, 
        inner_radius, 
        segment_length, 
        space
    )

    tile = (
        cq.Workplane("XY")
        .union(outline)
        .add(tile_pipe)
    )

    return tile




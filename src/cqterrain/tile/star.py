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

import cadquery as cq
from cadqueryhelper import shape

def star(length=10, width=10, height=1, points=4, outer_radius=5, inner_radius=3, padding=.5):
    tile = cq.Workplane("XY").box(length, width, height)

    cut_star = shape.star(outer_radius=outer_radius+(padding/2), inner_radius=inner_radius+(padding/2), points=points, height=height)
    star = shape.star(outer_radius=outer_radius-(padding/2), inner_radius=inner_radius-(padding/2), points=points, height=height)

    return tile.cut(cut_star).add(star)

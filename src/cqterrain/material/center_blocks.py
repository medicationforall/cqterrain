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
from typing import List

def center_blocks(blocks:cq.Workplane) -> List[cq.Workplane]:
    split_blocks = blocks.solids().vals()
    c_blocks = []
    for s_block in split_blocks:
        bound_center = s_block.CenterOfBoundBox() #type:ignore
        location = cq.Location((-bound_center.x,-bound_center.y,0))
        scene = cq.Workplane("XY").add(s_block.located(location)) #type:ignore
        c_blocks.append(scene)
    return c_blocks
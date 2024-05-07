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

import cadquery as cq
import math
from cadqueryhelper import series

def slot(
length:float = 10,
width:float = 10,
height:float = 2,
padding:float = 1,
slot_length_padding:float = 3,
slot_width_offset:float = 1.5,
slot_width:float = 1,
slot_height:float = 0.5
) -> cq.Workplane:
    tile = (
        cq.Workplane("XY")
        .box(length-padding, width-padding, height)
    )

    slot = (
        cq.Workplane("XY")
        .slot2D(length - slot_length_padding, slot_width)
        .extrude(height + slot_height))
    slot_count = math.floor((width - padding) / (slot_width + slot_width_offset))
    if slot_count > 1:
        slots = series(
            shape = slot,
            size = slot_count,
            width_offset = slot_width_offset
        )
    else:
        slots = slot
    return tile.cut(slots.translate((0, 0, -1*((height + slot_height)/2))))

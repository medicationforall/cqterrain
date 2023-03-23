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

def glyph(length = 4, width = 2, height = 1, padding = 2):
    width_padding = width + padding
    bricks = __brick_tile(length, width, height, padding)

    combine = (
        cq.Workplane("XY")
        .union(
            bricks
            .translate((-1*(length/2+padding),0,0))
        )
        .union(
            bricks
            .rotate((0,0,1),(0,0,0),90)
            .translate(((length/2+padding),0,0))
        )
    )

    tile_combine = (
        cq.Workplane("XY")
        .union(
            combine
            .translate((0,-1*width_padding,0))
        )
        .union(
            combine
            .rotate((0,0,1),(0,0,0), 180)
            #.translate((0,width_padding,0))
        )
    )
    return tile_combine.translate((0,(width_padding/2),0))

def __brick_tile(length = 4, width = 2, height = 1, padding = .5):
    length_padding = length + padding
    width_padding = width + padding
    rect = (
            cq.Workplane("XY")
            .box(width, length_padding, height)
            .center(width_padding, 0)
            .box(width, length_padding, height)
            .translate((-1*(width_padding/2), 0, 0))
            )
    return rect

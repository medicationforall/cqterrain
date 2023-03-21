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

def windmill(tile_size=10, height=1, padding=.5):
    outline = cq.Workplane("XY").box(tile_size, tile_size, height)
    sq_size = (tile_size/3)-padding/2
    rec_size = ((tile_size/3)*2)
    square = cq.Workplane("XY").box(sq_size, sq_size, height)
    rectangle = cq.Workplane("XY").box(sq_size, rec_size, height)

    rec_tran = rectangle.translate((sq_size+padding,sq_size/2+padding/2,0))
    tile = (
        square
        .union(rec_tran)
        .union(rec_tran.rotate((0,0,1),(0,0,0),90))
        .union(rec_tran.rotate((0,0,1),(0,0,0),180))
        .union(rec_tran.rotate((0,0,1),(0,0,0),270))
    )
    return outline.intersect(tile)

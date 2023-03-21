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

def rivet(
    length = 10,
    width = 10,
    height = 2,
    padding = 1,
    internal_padding = 2.5,
    rivet_height = 2.5,
    rivet_radius = .5
):
    tile = (
        cq.Workplane("XY")
        .box(length-padding, width-padding, height)
    )

    internal_tile = (
        cq.Workplane("XY")
        .box(length-internal_padding, width-internal_padding, height)
        .faces("not Y")
        .edges("Z")
        .cylinder(rivet_height, rivet_radius)
    )
    return tile.add(internal_tile)

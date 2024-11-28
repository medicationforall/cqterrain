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
# limitations under the License.

import cadquery as cq
from . import pipe_face
from cqterrain.barrier import (
    barrier_straight,
    cut_magnets
)

def straight(
        length:float = 75, 
        connector_length:float = 2, 
        connector_radius:float = 11.5,
        render_hollow:bool = True,
        hollow_padding:float = 6,
        hollow_radius_padding:float = 3,
        render_through_hole:bool = True,
        through_radius:float = 5,
        debug_magnets:bool = False
    ) -> cq.Workplane:
    connector_plate = cq.Workplane("XY").cylinder(connector_length, connector_radius).rotate((0,1,0),(0,0,0),90).translate((0,0,connector_radius+.5))
    outline = pipe_face()
    barrier = barrier_straight(
        j_shape = outline,
        length = length
    ).translate((0,0,23/2))

    x_translate = (length/2)-connector_length/2
    barrier_plates = (
        cq.Workplane("XY")
        .union(barrier)
        .union(connector_plate)
        .union(connector_plate.translate((x_translate,0,0)))
        .union(connector_plate.translate((-x_translate,0,0)))
    )

    barrier_plates_magnets = cut_magnets(
        barrier_plates,
        y_offset = 0,
        z_lift = 6,
        debug = debug_magnets
    )
    
    if render_hollow:
        center_cut = (
            cq.Workplane("XY")
            .cylinder(
                length-hollow_padding,
                connector_radius-hollow_radius_padding
            )
            .rotate((0,1,0),(0,0,0),90)
            .translate((0,0,connector_radius))
        )
        barrier_plates_magnets = barrier_plates_magnets.cut(center_cut)
        
    if render_through_hole:
        through_cut = (
            cq.Workplane("XY")
            .cylinder(
                length,
                through_radius
            )
            .rotate((0,1,0),(0,0,0),90)
            .translate((0,0,connector_radius))
        )
        barrier_plates_magnets = barrier_plates_magnets.cut(through_cut)

    return barrier_plates_magnets
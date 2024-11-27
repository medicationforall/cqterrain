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
from ..walkway import Walkway
from . import straight
from ..stairs import industrial_stairs


def platform(
        top_length = 42, 
        stair_y_distance = 23,
        straight_pipe = None,
        render_hollow = True,
        render_through_hole = True
    ):

    if not straight_pipe:
        straight_pipe = straight(
            render_hollow = render_hollow, 
            render_through_hole = render_through_hole
        )

    stairs = industrial_stairs(
        length=24.5, 
        width = top_length - 2,
        stair_count=3
    ).faces("<Z").edges("<X").chamfer(14)
    
    walk_bp = Walkway()
    walk_bp.length = top_length
    walk_bp.width = 35
    walk_bp.render_rails = False 
    walk_bp.render_tabs = False 
    walk_bp.slots_end_margin = 2
    walk_bp.slot_width_padding = 3 
    walk_bp.make()
    walk = walk_bp.build()
    
    group = (
        cq.Workplane()
        .union(straight_pipe)
        .union(stairs.rotate((0,0,1),(0,0,0),-90).translate((0,stair_y_distance,75/2)))
        .union(stairs.rotate((0,0,1),(0,0,0),90).translate((0,-stair_y_distance,75/2)))
        .union(walk.translate((0,0,22)))
    )
    return group

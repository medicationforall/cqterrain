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

def pull_handle(
    length:float = 3, 
    width:float = 4, 
    height:float = 6,
    handle_length:float = 1,
    handle_width_padding:float = 1,
    handle_z_margin:float = 2,
    handle_base_chamfer:float = 1,
    mirrored:bool = False
) -> cq.Workplane:
    plate = (
        cq.Workplane("XY")
        .box(length,width,height)
    )
    
    handle = (
        cq.Workplane("XY")
        .box(
            handle_length, 
            width+handle_width_padding*2, 
            height -handle_z_margin/2
        ).faces("-Z").edges("X").chamfer(handle_base_chamfer)
    )
    
    handle_cut = (
        cq.Workplane("XY")
        .box(
            handle_length+handle_width_padding, 
            width+handle_width_padding, 
            height-handle_z_margin-handle_width_padding
        )
    )
    
    handle_combined = (
        cq.Workplane("XY")
        .union(handle.translate((0,0,-(handle_z_margin/4))))
        .cut(handle_cut)
    )
    
    if mirrored == False:
        cut_box = (
            cq.Workplane("XY")
            .box(
                handle_length, 
                width+handle_width_padding*2, 
                height -handle_z_margin/2
            )
            .translate((0,((width+handle_width_padding*2)/2),-(handle_z_margin/4)))
        )
        handle_combined = handle_combined.cut(cut_box)
    
    plate = plate.union(handle_combined)
    return plate
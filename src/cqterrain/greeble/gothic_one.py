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
# limitations under the License.

import cadquery as cq
from cadqueryhelper.shape import diamond as shape_diamond

def gothic_one(
    length:float = 15,
    width:float = 4,
    height:float = 20,
    frame_size:float = .5,
    pane_width:float = 1,
    inside_frame_width:float = -.5,
    inside_frame_size:float = .5,
    diamond_frame_size:float = 1,
    diamond_frame_width:float = -.25,
    diamond_inside:float = -.5
) -> cq.Workplane:
    tile = (
        cq.Workplane("XY")
        .box(length, width, height)
    )
    
    inside_cut = (
        cq.Workplane("XY")
        .box(
            length-(frame_size*2), 
            width, 
            height-(frame_size*2)
        )
    )
    
    inside_frame = (
        cq.Workplane("XY")
        .box(
            length-(frame_size*2), 
            width + (inside_frame_width*2), 
            height-(frame_size*2)
        )
    )
    
    inside_frame_cut = (
        cq.Workplane("XY")
        .box(
            length-(frame_size*2)-(inside_frame_size*2), 
            width + (inside_frame_width*2), 
            height-(frame_size*2)-(inside_frame_size*2)
        )
    )
    
    diamond = shape_diamond(
        length = length-(frame_size*2)-(inside_frame_size*2),
        width = height-(frame_size*2)-(inside_frame_size*2),
        height = width + (inside_frame_width*2) + (diamond_frame_width*2)
    ).rotate((1,0,0),(0,0,0),90)
    
    diamond_cut = shape_diamond(
        length = length-(frame_size*2)-(inside_frame_size*2) -(diamond_frame_size*2),
        width = height-(frame_size*2)-(inside_frame_size*2) -(diamond_frame_size*2),
        height = width + (inside_frame_width*2) + (diamond_frame_width*2)
    ).rotate((1,0,0),(0,0,0),90)
    
    diamond_frame = (
        cq.Workplane("XY")
        .union(diamond)
        .cut(diamond_cut)
    )
    
    diamond_inside_pane = shape_diamond(
        length = length-(frame_size*2)-(inside_frame_size*2) -(diamond_frame_size*2),
        width = height-(frame_size*2)-(inside_frame_size*2) -(diamond_frame_size*2),
        height = width + (inside_frame_width*2) + (diamond_frame_width*2) + (diamond_inside*2)
    ).rotate((1,0,0),(0,0,0),90)
    
    ellipse_extrude = width + (inside_frame_width*2) + (diamond_frame_width*2) + (diamond_inside*2)
    ellipse_x_radius = (length-(frame_size*2)-(inside_frame_size*2) -(diamond_frame_size*2))/6
    ellipse_y_radius = (height-(frame_size*2)-(inside_frame_size*2) -(diamond_frame_size*2))/6
    ellipse = (
        cq.Workplane("XY" )
        .ellipse(
            ellipse_x_radius,
            ellipse_y_radius
        ).extrude(ellipse_extrude).translate((0,0,-(ellipse_extrude/2))).rotate((1,0,0),(0,0,0),90)
    )
    
    ellipse_2 = (
        cq.Workplane("XY" )
        .ellipse(
            ellipse_x_radius,
            ellipse_y_radius
        ).extrude(ellipse_extrude).translate((0,0,-(ellipse_extrude/2))).rotate((1,0,0),(0,0,0),90)
    )
    
    inside_pane =  (
        cq.Workplane("XY")
        .box(
            length-(frame_size*2), 
            pane_width, 
            height-(frame_size*2)
        )
    )
    
    combi = (
        cq.Workplane("XY")
        .union(tile)
        .cut(inside_cut)
        .union(inside_frame)
        .cut(inside_frame_cut)
        .union(diamond_frame)
        .add(diamond_inside_pane)
        .cut(ellipse.translate((0,0,ellipse_y_radius)))
        .cut(ellipse.translate((0,0,-(ellipse_y_radius))))
        .cut(ellipse_2.translate((ellipse_x_radius,0,0)))
        .cut(ellipse_2.translate((-(ellipse_x_radius),0,0)))
        .union(inside_pane)
    )
    return combi
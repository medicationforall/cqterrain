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
import math
from cadqueryhelper import shape, series

def jersey_shape(
    width:float = 10,
    height:float = 10,
    base_height:float = 2,
    middle_width_inset:float = -2,
    middle_height:float = 2,
    top_width_inset:float = -1
) -> cq.Workplane:
    mid_height = base_height + middle_height
    top_width = middle_width_inset + top_width_inset
    pts = [
        (0,0),
        (0,width),# base width
        (base_height,width),#base Height
        (mid_height, width + middle_width_inset), # middle

        (height,width + top_width),# top
        (height,-1*(top_width)),# top

        (mid_height, -1*(middle_width_inset)), # middle
        (base_height,0)
    ]

    result = (
        cq.Workplane("XY")
        .center(-1*(height/2),-1*(width/2))
        .polyline(pts)
        .close()
    )
    return result

def barrier_straight(
    j_shape:cq.Workplane,#non-optional
    length:float = 10
):
    j_barrier = (
        j_shape
        .extrude(length)
        .translate((0,0,-1*(length/2)))
        .rotate((0,1,0),(0,0,0),90)
    )
    return j_barrier

def barrier_curved(
    j_shape:cq.Workplane,
    x_radius:float = 75,
    y_radius:float = 75,#ellipse stretch
    angle:float = 270,
    rotation_angle:float = 0
):
    path = (
        cq.Workplane("ZY")
        .ellipseArc(
            x_radius,
            y_radius,
            angle,
            rotation_angle=rotation_angle
        )
    )

    return (
        j_shape
        .toPending()
        .sweep(path)
        .rotate((0,1,0),(0,0,0),90)
        .translate((x_radius/2,-1*(y_radius/2),0))
    )

def barrier_diagonal(
    j_shape:cq.Workplane,
    x:float = 75,
    y:float = 37.5,
    axis:str = "ZY"
):
    path = cq.Workplane(axis).lineTo(x,y)
    result = j_shape.toPending().sweep(path)
    return result.rotate((0,1,0),(0,0,0),90)

def taper_barrier(
    straight_barrier:cq.Workplane,
    length:float = 75,
    width:float = 20,
    height:float = 20,
    rotation:float =-12.8,
    z_offset:float = 3,
    length_padding:float = 2,
    debug:bool = False
):
    length_combined = length + length_padding
    taper_block = (
        cq.Workplane("XY")
        .box(length_combined, width, height)
        .translate((-1*(length_combined/2),0,(height/2)))
        .rotate((0,1,0),(0,0,0),rotation)
        .translate(((length/2),0,z_offset))

    )
    barrier_taper = (
        cq.Workplane("XY")
        .add(straight_barrier)
    )

    if debug:
        barrier_taper = barrier_taper.add(taper_block)
    else:
        barrier_taper = barrier_taper.cut(taper_block)

    return barrier_taper

def __extrude_faces(
        shape:cq.Workplane,
        extrude:float = 10,
        faces:int = 4,
        intersect:bool = True
    ):
    poly = (
        shape
        .toPending()
        .extrude(extrude)
        .translate((0,0,-1*(extrude/2)))
    )

    mirror = (
        cq.Workplane("XY")
        .union(poly)
        .union(poly.rotate((1,0,0),(0,0,0),180))
    )

    rotate_degrees = math.floor(360 / faces)
    rotations = int(faces/2)

    scene = (
        cq.Workplane("XY")
        .union(mirror)
    )
    for i in range(rotations):
        if i == 0:
            scene = scene.union(mirror)
        else:
            if intersect:
                scene = scene.intersect(mirror.rotate((1,0,0),(0,0,0),rotate_degrees*i))
            else:
                scene = scene.union(mirror.rotate((1,0,0),(0,0,0),rotate_degrees*i))

    return scene.rotate((0,1,0),(0,0,0),90)

def barrier_cross(
        j_shape:cq.Workplane, 
        extrude:float = 20, 
        faces:int = 4, 
        intersect:bool = False
    ):
    corner = __extrude_faces(
        j_shape,
        extrude=extrude,
        faces=faces,
        intersect=intersect
    )

    return corner


def cut_forklift(
        barrier:cq.Workplane,
        length:float = 75,
        fork_length:float = 5,
        width:float = 20,
        fork_height:float = 2
):
    fork_cut = (
        cq.Workplane("XY")
        .box(fork_length, width, fork_height)
        .translate((0,0,fork_height/2))
    )
    result = (
        cq.Workplane("XY")
        .add(barrier)
        .cut(fork_cut.translate((length/4,0,0)))
        .cut(fork_cut.translate((-1*(length/4),0,0)))
    )
    return result

def cut_magnets(
    barrier:cq.Workplane,
    width:float = 20,
    pip_height:float = 2.4,
    pip_radius:float = 1.56,
    x_plus_cut:bool = True,
    x_minus_cut:bool = True,
    y_offset:float = 0,
    z_lift:float = 1.5,
    debug:bool = False
):
    pip = (
        cq.Workplane("XY")
        .cylinder(pip_height,pip_radius)
        .rotate((0,1,0),(0,0,0),90)
    )
    x_face = barrier.faces(">X").workplane().val().Center() #type:ignore

    cuts = (
        cq.Workplane("XY")
        .add(pip.translate((
            x_face.x - (pip_height/2),
            -1*((width/2) - pip_radius - 2),
            pip_radius + z_lift
        )))
        .add(pip.translate((
            x_face.x - (pip_height/2),
            ((width/2) - pip_radius - 2),
            pip_radius + z_lift
        )))
    )

    result  = (
        cq.Workplane("XY")
        .add(barrier)
    )

    if x_plus_cut:
        if debug:
            result = result.add(cuts.translate((0,-y_offset,0)))
        else:
            result = result.cut(cuts.translate((0,-y_offset,0)))

    if x_minus_cut:
        if debug:
            result = result.add(cuts.rotate((0,0,1),(0,0,0),180).translate((0,-y_offset,0)))
        else:
            result = result.cut(cuts.rotate((0,0,1),(0,0,0),180).translate((0,-y_offset,0)))
    return result

def caution_stripe(
        length:float = 50,
        width:float = 10,
        height:float = 10,
        stripe_padding:float = .4,
        bar_width:float = 5,
        bar_padding:float = 1,
        bar_inset:float = 1.5,
        z_offset:float = -.2
):
    bar = (
        shape.rail(
            width,
            height,
            bar_width,
            bar_width-bar_inset
        )
        .rotate((1,0,0),(0,0,0),90)
        .rotate((0,0,1),(0,0,0),90)
    )


    bar_space = bar_width + bar_padding*2
    size = math.floor(length/bar_space)
    bars = series(
        bar,
        length_offset=bar_padding*2,
        size=size
    )

    stripe = (
        cq.Workplane("XY")
        .box(
            length,
            width-stripe_padding,
            height-stripe_padding*4)
        .union(bars.translate((
            0,
            stripe_padding + z_offset,
            0
        )))
        .rotate((1,0,0),(0,0,0),-90)
    ).translate((0,0,z_offset))

    return stripe

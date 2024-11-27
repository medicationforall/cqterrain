import cadquery as cq
import math

from cqterrain.barrier import (
    jersey_shape,
    barrier_straight,
    barrier_cross,
    barrier_curved,
    barrier_diagonal,
    taper_barrier
)

barrier_height = 20

j_shape = jersey_shape(
    width = 20,
    height = barrier_height,
    base_height = 4,
    middle_width_inset = -5,
    middle_height = 4,
    top_width_inset = -1
)

j_shape_template = jersey_shape(
    width = 23,
    height = barrier_height+3,
    base_height = 4+3,
    middle_width_inset = -5,
    middle_height = 4,
    top_width_inset = -1
)

j_shape_cut = jersey_shape(
    width = 20.4,
    height = barrier_height+.4,
    base_height = 4+.4,
    middle_width_inset = -5,
    middle_height = 4,
    top_width_inset = -1
)


barrier = barrier_straight(
    j_shape = j_shape,
    length = 75
).translate((0,0,barrier_height/2))

barrier_two = barrier_straight(
    j_shape = j_shape_template.toPending(),
    length = 6
).rotate((0,1,0),(0,0,0),90)

barrier_cut = barrier_straight(
    j_shape = j_shape_cut.toPending(),
    length = 6
).rotate((0,1,0),(0,0,0),90)

barrier_standin = barrier_straight(
    j_shape = j_shape.toPending(),
    length = 6
).rotate((0,1,0),(0,0,0),90)

pip_height = 2.1
pip_radius = 1.55
magnet_template_cut = (
    cq.Workplane("XY")
    .cylinder(6,pip_radius)
)

barrier_template = (
    cq.Workplane("XY")
    .add(barrier_two)
    .cut(magnet_template_cut.translate((
        (barrier_height/2)-pip_radius-1.5,
        (20/2)-pip_radius-2,
        0
    )))
    .cut(magnet_template_cut.translate((
        ((barrier_height/2)-pip_radius-1.5),
        -1*((20/2)-pip_radius-2),
        0
    )))
    .cut(barrier_cut.translate((0,0,3)))
    #.add(barrier_standin.translate((0,0,3)))
)

scene = (
    cq.Workplane("XY")
    .add(barrier_template)
)

#show_object(scene)

cq.exporters.export(barrier_template, 'stl/barrier_magnet_template.stl')

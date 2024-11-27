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

barrier = barrier_straight(
    j_shape = j_shape,
    length = 75
).translate((0,0,barrier_height/2))

barrier_curve_90 = (
    barrier_curved(
        j_shape,
        x_radius = 75,
        y_radius = 75,#ellipse stretch
        angle = 270,
        rotation_angle=0
    )
    .translate((0,0,barrier_height/2))
)

barrier_curve_45 = (
    barrier_curved(
        j_shape,
        x_radius = 75,
        y_radius = 75,#ellipse stretch
        angle = 315,
        rotation_angle=-45
    )
    .translate((0,0,barrier_height/2))
)

barrier_curve_60 = (
    barrier_curved(
        j_shape,
        x_radius = 75,
        y_radius = 75,#ellipse stretch
        angle = 300,
        rotation_angle=-30
    )
    .translate((0,0,barrier_height/2))
)

barrier_taper = taper_barrier(
    barrier,
    length = 75,
    debug = False
)

barrier_diag_right = (
    barrier_diagonal(
        j_shape,
        x = 75,
        y = 37.5,
        axis = "ZY"
    ).translate(((75/2),-1*(37.5/2),barrier_height/2))
)

barrier_diag_right_short = (
    barrier_diagonal(
        j_shape,
        x = 37.5,
        y = 18.75,
        axis = "ZY"
    ).translate(((37.5/2),-1*(18.75/2),barrier_height/2))
)

barrier_diag_left = (
    barrier_diagonal(
        j_shape,
        x = -75,
        y = 37.5,
        axis = "ZY"
    ).translate((-1*(75/2),-1*(37.5/2),barrier_height/2))
)

barrier_diag_left_short = (
    barrier_diagonal(
        j_shape,
        x = -37.5,
        y = 18.75,
        axis = "ZY"
    ).translate((-1*(37.5/2),-1*(18.75/2),barrier_height/2))
)

barrier_c = barrier_cross(j_shape).translate((0,0,barrier_height/2))

scene = (
    cq.Workplane("XY")
    .add(barrier)
    ##.add(barrier_curve_90.translate((0,-50,0)))
    ##.add(barrier_curve_45.translate((0,-80,0)))
    .add(barrier_curve_60.translate((0,-35,0)))
    .add(barrier_taper.translate((0,25,0)))
    .add(barrier_diag_right.translate((0,70,0)))
    ##.add(barrier_diag_right_short.translate((0,95,0)))
    ##.add(barrier_diag_left_short.translate((0,135,0)))
    .add(barrier_diag_left.translate((0,130,0)))
    .add(barrier_c.translate((0,-25,0)))
)

#show_object(scene)

cq.exporters.export(barrier, 'stl/barrier.stl')
cq.exporters.export(barrier_taper, 'stl/barrier_taper.stl')
cq.exporters.export(barrier_c, 'stl/barrier_c.stl')

##cq.exporters.export(barrier_curve_45, 'stl/barrier_curve_45.stl')
##cq.exporters.export(barrier_curve_90, 'stl/barrier_curve_90.stl')
cq.exporters.export(barrier_curve_60, 'stl/barrier_curve_60.stl')

##cq.exporters.export(barrier_diag_right_short, 'stl/barrier_diag_right_short.stl')
##cq.exporters.export(barrier_diag_left_short, 'stl/barrier_diag_left_short.stl')
cq.exporters.export(barrier_diag_right, 'stl/barrier_diag_right.stl')
cq.exporters.export(barrier_diag_left, 'stl/barrier_diag_left.stl')

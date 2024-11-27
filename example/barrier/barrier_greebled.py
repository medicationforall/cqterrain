import cadquery as cq
import math

from cqterrain.barrier import (
    jersey_shape,
    barrier_straight,
    barrier_cross,
    barrier_curved,
    barrier_diagonal,
    taper_barrier,
    cut_forklift,
    cut_magnets,
    caution_stripe
)

barrier_height = 25
barrier_width = 20


j_shape = jersey_shape(
    width = barrier_width,
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

barrier_forks = cut_forklift(barrier)
barrier_forks_m = cut_magnets(
    barrier_forks,
    y_offset=0)

barrier_curve_60 = (
    barrier_curved(
        j_shape,
        x_radius = 75,
        y_radius = 75,#ellipse stretch
        angle = 300,
        rotation_angle=-30
    )
    .translate((0,0,barrier_height/2))
    .rotate((0,0,1),(0,0,0),-30)
    .translate((-1*(13.5),0,0))
)

barrier_curve_60_forks = cut_forklift(
    barrier_curve_60,
    width = 80
)

barrier_curve_60_forks = (
    barrier_curve_60_forks
    .rotate((0,0,1),(0,0,0),30)
    .translate((0,31,0))
)

barrier_curve_60_forks_m = cut_magnets(
    barrier_curve_60_forks,
    x_minus_cut=False
).rotate((0,0,1),(0,0,0),120).translate((0,-15,0))

barrier_curve_60_forks_m = cut_magnets(
    barrier_curve_60_forks_m,
    x_minus_cut=False
).rotate((0,0,1),(0,0,0),-150).translate((0,-30,0))

barrier_taper = taper_barrier(
    barrier,
    length = 78,
    height = barrier_height,
    rotation=-16.04,
    debug = False
)

barrier_taper_forks = cut_forklift(barrier_taper)
barrier_taper_forks_m = cut_magnets(barrier_taper_forks,x_plus_cut=False)

barrier_diag_right = (
    barrier_diagonal(
        j_shape,
        x = 75,
        y = 37.5,
        axis = "ZY"
    ).translate(((75/2),-1*(37.5/2),barrier_height/2))
    .rotate((0,0,1),(0,0,0),-1*(53/2))
)

barrier_diag_right_forks = cut_forklift(
    barrier_diag_right
).rotate((0,0,1),(0,0,0),(53/2))

barrier_diag_right_forks_m = cut_magnets(
    barrier_diag_right_forks,
    x_minus_cut = False,
    y_offset = 18.5
)

barrier_diag_right_forks_m = cut_magnets(
    barrier_diag_right_forks_m.rotate((0,0,1),(0,0,0),180),
    x_minus_cut = False,
    y_offset = 18.5
).rotate((0,0,1),(0,0,0),-1*(53/2))

barrier_diag_left = (
    barrier_diagonal(
        j_shape,
        x = -75,
        y = 37.5,
        axis = "ZY"
    ).translate((-1*(75/2),-1*(37.5/2),barrier_height/2))
    .rotate((0,0,1),(0,0,0),(53/2))
)

barrier_diag_left_forks = cut_forklift(
    barrier_diag_left
).rotate((0,0,1),(0,0,0),-1*(53/2))

barrier_diag_left_forks_m = cut_magnets(
    barrier_diag_left_forks,
    x_minus_cut = False,
    y_offset = -18.5
)

barrier_diag_left_forks_m = cut_magnets(
    barrier_diag_left_forks_m.rotate((0,0,1),(0,0,0),180),
    x_minus_cut = False,
    y_offset = -18.5
).rotate((0,0,1),(0,0,0),(53/2))

barrier_c = barrier_cross(j_shape).translate((0,0,barrier_height/2))
barrier_c_m = cut_magnets(barrier_c)
barrier_c_m = cut_magnets(barrier_c_m.rotate((0,0,1),(0,0,0),90))

caution = caution_stripe(length=65, width = 17, height=10)

detail_cut = (
    cq.Workplane("XY")
    .box(65,10,17)
)
detailed_barrier = (
    cq.Workplane("XY")
    .add(barrier_forks_m.translate((0,0,-barrier_height/2)))
    .cut(detail_cut.translate((0,0,4)))
    .add(caution.translate((0,0,4)))
).translate((0,0,barrier_height/2))

scene = (
    cq.Workplane("XY")
    .add(barrier_c_m.translate((0,-80,0)))
    .add(barrier_curve_60_forks_m.translate((8,-43,0)))
    .add(barrier_forks_m.translate((0,-25,0)))
    .add(detailed_barrier)
    .add(barrier_taper_forks_m.translate((0,25,0)))
    .add(barrier_diag_right_forks_m.translate((0,47,0)))
    .add(barrier_diag_left_forks_m.translate((0,67,0)))
)

#show_object(scene)

# Print These
cq.exporters.export(barrier_c_m, 'stl/barrier_c.stl')
cq.exporters.export(barrier_curve_60_forks_m, 'stl/barrier_curve_60.stl')
cq.exporters.export(barrier_forks_m, 'stl/barrier.stl')
cq.exporters.export(detailed_barrier, 'stl/barrier_detailed.stl')
cq.exporters.export(barrier_taper_forks_m, 'stl/barrier_taper.stl')
cq.exporters.export(barrier_diag_right_forks_m, 'stl/barrier_diag_right.stl')
cq.exporters.export(barrier_diag_left_forks_m, 'stl/barrier_diag_left.stl')

## legacy
##cq.exporters.export(barrier_curve_45, 'stl/barrier_curve_45.stl')
##cq.exporters.export(barrier_curve_90, 'stl/barrier_curve_90.stl')

##cq.exporters.export(barrier_diag_right_short, 'stl/barrier_diag_right_short.stl')
##cq.exporters.export(barrier_diag_left_short, 'stl/barrier_diag_left_short.stl')

import cadquery as cq
from cqterrain.damage import uneven_plane, uneven_spline_plane

u_plane_risky = uneven_spline_plane(
    length=20, 
    width=25,
    height=4,
    peak_count=(5,6),

    segments=5,
    seed='test',
    render_plate=True,
    plate_height = 0.1
)

# show_object(u_plane_risky)

cq.exporters.export(u_plane_risky, "stl/damage_uneven_spline_plane_risky.stl")
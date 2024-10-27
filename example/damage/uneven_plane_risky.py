import cadquery as cq
from cqterrain.damage import uneven_plane

u_plane_risky = uneven_plane(
    length=300, 
    width=350,
    height=40,
    step=20,
    peak_count=(4,5),
    #peak_count=5,
    segments=5,
    seed='test_4',
    render_plate=True,
    plate_height = 0.1
)

#show_object(u_plane_safe)
cq.exporters.export(u_plane_risky, "stl/damage_uneven_plane_risky.stl")

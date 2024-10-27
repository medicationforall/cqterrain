import cadquery as cq
from cqterrain.damage import uneven_plane

u_plane_safe = uneven_plane(
    length=20, 
    width=25,
    height=4,
    #peak_count=(3,5),
    peak_count=5,

    segments=5,
    seed='test',
    render_plate=True,
    plate_height = 0.1
)

#show_object(u_plane_safe)
cq.exporters.export(u_plane_safe, "stl/damage_uneven_plane_safe.stl")


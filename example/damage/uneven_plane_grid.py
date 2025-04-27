import cadquery as cq
from cqterrain.damage import uneven_plane

#grid of surfaces
seed='test_2'

def add_surface(loc:cq.Location) -> cq.Shape:
    u_plane_risky = uneven_plane(
        length = 60, 
        width = 35,
        height = 5,
        peak_count = (4,5),
        step = .5,
        #peak_count=5,
        segments = 5,
        seed = None,
        render_plate = True,
        plate_height = 0.1
    )
    return u_plane_risky.val().located(loc) #type:ignore

uneven_surface_example = (
    cq.Workplane("XY")
    .rarray(
        xSpacing = 70, 
        ySpacing = 40,
        xCount = 5, 
        yCount= 5, 
        center = True)
    .eachpoint(add_surface)
)

#show_object(uneven_surface_example)
cq.exporters.export(uneven_surface_example, "stl/damage_uneven_plane_grid.stl")
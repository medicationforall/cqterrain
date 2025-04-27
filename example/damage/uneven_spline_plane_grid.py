import cadquery as cq
from cqterrain.damage import uneven_spline_plane

#grid of surfaces
seed='test'

def add_surface(loc:cq.Location) -> cq.Shape:
    u_plane_risky = uneven_spline_plane(
        length = 90, 
        width = 90,
        height = 9,
        #peak_count = (4,5),
        peak_count=5,
        min_height = 2,
        step = 1,
        
        segments = 6,
        seed = None,
        render_plate = True,
        plate_height = 0.5
    )
    return u_plane_risky.val().located(loc) #type:ignore

uneven_surface_example = (
    cq.Workplane("XY")
    .rarray(
        xSpacing = 100, 
        ySpacing = 100,
        xCount = 3, 
        yCount= 3, 
        center = True)
    .eachpoint(add_surface)
)

#show_object(uneven_surface_example)
cq.exporters.export(uneven_surface_example, "stl/damage_uneven_spline_plane_grid.stl")
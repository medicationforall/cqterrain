import cadquery as cq
from . import rectangle
from ..damage import uneven_plane

def rectangle_uneven(
        length = 40,
        width = 40,
        base_height=3,
        taper = -1,
        render_magnet = True,  
        magnet_diameter = 3, 
        magnet_height = 2,
        detail_height=3,
        uneven_height=4,
        peak_count = (9,10),
        segments=6,
        seed="seed"
    ):
    # slot
    mini_base = rectangle(
        length = length,
        width = width,
        height = base_height, 
        taper = taper,
        render_magnet = render_magnet,  
        magnet_diameter = magnet_diameter, 
        magnet_height = magnet_height
    ).rotate((0,0,1),(0,0,0),90)

    top = (
           mini_base
           .faces("Z")
           .wires()
           .toPending()
           .extrude(detail_height)
           )
    
    # uneven plane
    u_plane_safe = uneven_plane(
        length = length, 
        width = width,
        height = uneven_height,
        peak_count = peak_count,
        segments = segments,
        seed = seed,
        render_plate = True,
        plate_height = 0.1
    )
        
    u_plane_safe = u_plane_safe.translate((0,0,base_height/2 + uneven_height/2))

    scene = (
        cq.Workplane("XY")
        .union(top)
        .intersect(u_plane_safe)
        .add(mini_base)
    )
    
    return scene
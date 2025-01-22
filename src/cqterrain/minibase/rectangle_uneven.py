import cadquery as cq
from . import rectangle
from ..damage import uneven_plane

def rectangle_uneven(
        length:float = 40,
        width:float = 40,
        base_height:float = 3,
        taper:float = -1,
        render_magnet:bool = True,  
        magnet_diameter:float = 3, 
        magnet_height:float = 2,
        detail_height:float = 3,
        uneven_height:float = 4,
        peak_count:tuple[int,int]|int = (9,10),
        segments:int = 6,
        seed:str = "seed"
    ) -> cq.Workplane:
    # slot
    mini_base = rectangle(
        length = length,
        width = width,
        height = base_height, 
        taper = taper,
        render_magnet = render_magnet,  
        magnet_diameter = magnet_diameter, 
        magnet_height = magnet_height
    )

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
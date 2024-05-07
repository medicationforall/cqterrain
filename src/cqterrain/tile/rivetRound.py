import cadquery as cq
from typing import Callable

def __add_shape(
        custom_shape:cq.Workplane, 
        padding:float = 0, 
        height:float = 0, 
        rivet_height:float = 2
    ) -> Callable[[cq.Location], cq.Shape]:
    def add_shape(loc:cq.Location) ->cq.Shape:
        nonlocal custom_shape
        nonlocal padding
        nonlocal height
        nonlocal rivet_height
        return custom_shape.translate((-2,0,height/2+rivet_height/2)).val().located(loc) #type:ignore
    return add_shape

def rivet_round(
        radius:float = 10, 
        height:float = 2,
        rivet_height:float = 0.5,
        rivet_radius:float = .5,
        padding:float = 1,
        rivet_count:int = 5
) -> cq.Workplane:
    base = cq.Workplane("XY").cylinder(height, radius)
    rivet = cq.Workplane("XY").cylinder(rivet_height, rivet_radius)
    rivets =(
        cq.Workplane("XY")
        .polarArray(
            radius = radius, 
            startAngle = 0, 
            angle = 360, 
            count = rivet_count,
            fill = True,
            rotate = True
        )
        .eachpoint(callback = __add_shape(rivet, padding, height, rivet_height))  
    )
    return base.union(rivets)
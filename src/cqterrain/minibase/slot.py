import cadquery as cq
from . import make_magnet_outline

def slot(length=24, width=50, height=3, taper=-1, magnet_diameter=3, magnet_height=2):
    base = (
        cq.Workplane("XY" )
        .slot2D(width, length, 90)
        .workplane(offset=height)
        .slot2D(width+taper, length+taper, 90)
        .loft(combine=True)
        .translate((0,0,-1*(height/2)))
    )
    h_solid = make_magnet_outline(height, magnet_diameter,  magnet_height)
    return cq.Workplane("XY").add(base).cut(h_solid)
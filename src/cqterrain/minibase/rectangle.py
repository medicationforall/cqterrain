import cadquery as cq
from . import make_magnet_outline

def rectangle(length=25, width=25, height=3, taper=-1, magnet_diameter=3, magnet_height=2):
    base = (
        cq.Workplane("XY" )
        .rect(length, width)
        .workplane(offset=height)
        .rect(length+taper, width+taper)
        .loft(combine=True)
        .translate((0,0,-1*(height/2)))
    )

    h_solid = make_magnet_outline(height, magnet_diameter, magnet_height)

    return cq.Workplane("XY").add(base).cut(h_solid)
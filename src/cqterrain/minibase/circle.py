import cadquery as cq
from . import make_magnet_outline

def circle(diameter=25, height=3, taper=-1, magnet_diameter=3, magnet_height=2):
    b_base = diameter / 2
    b_top = b_base + taper
    b_solid = cq.Solid.makeCone(b_base, b_top, height).translate((0,0,-1*(height/2)))

    h_solid = make_magnet_outline(height, magnet_diameter,  magnet_height)
    return cq.Workplane("XY").add(b_solid).cut(h_solid)
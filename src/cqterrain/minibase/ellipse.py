import cadquery as cq
from . import make_magnet_outline

def ellipse(x_diameter=52, y_diameter=90, height=3, taper=-1, magnet_diameter=3, magnet_spacing=25, magnet_height=2):
    '''
    @todo should allow for multiple magnets
    '''
    base_x_radius = x_diameter / 2
    base_y_radius = y_diameter / 2

    top_x_radius = base_x_radius + taper
    top_y_radius = base_y_radius + taper

    base = (
        cq.Workplane("XY" )
        .ellipse(base_x_radius,base_y_radius)
        .workplane(offset=height)
        .ellipse(top_x_radius,top_y_radius)
        .loft(combine=True)
        .translate((0,0,-1*(height/2)))
    )

    h_solid = make_magnet_outline(height, magnet_diameter,  magnet_height)

    #magnet_count = math.floor(y_diameter/ magnet_spacing)
    #magnets = series.make_series(h_solid)
    #log(magnet_count)

    #return h_solid
    return cq.Workplane("XY").add(base).cut(h_solid)

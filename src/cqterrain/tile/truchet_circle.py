import cadquery as cq
from cadqueryhelper.shape import vase

def truchet_circle(
        length:float = 10,
        width:float = 10,
        height:float = 4,
        radius:float = 1.5, 
        base_height:float = 2,
        shift_design:float=0 #hack to deal with no square tiles
    ) -> cq.Workplane:
    circle = cq.Workplane('XY').circle(radius)
    torus_radius = length if length>width else width
    torus_radius = (torus_radius/2)
    
    torus = (
        vase(circle,radius=torus_radius)
        .rotate((0,1,0),(0,0,0),90)
        .translate((0,torus_radius,-(torus_radius/2)-shift_design))
    )
    
    base = cq.Workplane("XY").box(length,width,base_height)
    outline = cq.Workplane('XY').box(length,width,height)
    
    scene = (
        cq.Workplane("XY")
        .union(base.translate((0,0,base_height/2)))
        .union(torus.translate((torus_radius,torus_radius,0)))
        .union(torus.translate((-torus_radius,-torus_radius,0)))
        .intersect(outline.translate((0,0,height/2)))
    )
    
    return scene.translate((0,0,-(height/2)))
import cadquery as cq

def truchet_circle_three(
        length:float = 10,
        width:float = 10,
        radius:float = 1.5
    ) -> cq.Workplane:
    torus_radius = length if length>width else width
    torus_radius = (torus_radius/2)
    
    cylinder = cq.Workplane("XY").cylinder(radius*2, width/2+radius/2)
    in_cylinder = cq.Workplane("XY").cylinder(radius*2, width/2-radius/2)
    torus = cylinder.cut(in_cylinder)
    outline = cq.Workplane('XY').box(length,width,radius*2)
    
    scene = (
        cq.Workplane("XY")
        .add(torus.translate((width/2,width/2,0)))
        .intersect(outline)
        .translate((0,0,0))
    )
    
    scene = scene.union(scene.rotate((0,0,1),(0,0,0),180))
    return scene
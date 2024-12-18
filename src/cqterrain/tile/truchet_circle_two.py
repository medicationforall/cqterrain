import cadquery as cq

def truchet_circle_two(
        length:float = 10,
        width:float = 10,
        radius:float = 1.5
    ) -> cq.Workplane:
    torus_radius = length if length>width else width
    torus_radius = (torus_radius/2)
    
    torus = cq.Solid.makeTorus(torus_radius, radius)
    
    outline = cq.Workplane('XY').box(length,width,radius*2)
    
    scene = (
        cq.Workplane("XY")
        .add(torus.translate((torus_radius,torus_radius,0)))
        .intersect(outline)
    )
    
    scene = scene.union(scene.rotate((0,0,1),(0,0,0),180))
    return scene
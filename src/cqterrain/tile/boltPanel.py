import cadquery as cq

def bolt_panel(
        length=5, 
        width=6, 
        height = 2, 
        chamfer = .5, 
        radius_outer=.4,
        radius_internal=0.2,
        cut_height=0.25,
        padding = 1
    ):
    outline = (
        cq.Workplane("XY")
        .box(length, width, height)
    )
    
    if chamfer:
        outline = outline.faces("Z").chamfer(chamfer)
    
    cyl = (
        cq.Workplane("XY")
        .cylinder(height, radius_outer)
    )
    cyl_1 = (
        cq.Workplane("XY")
        .cylinder(height, radius_internal)
    )
    
    cyl_2 = (
        cq.Workplane("XY")
        .cylinder(height-cut_height, radius_outer)
    )
    
    cyl_i = (
        cq.Workplane("XY")
        .union(cyl_1)
        .add(cyl_2.translate((0,0,-cut_height/2)))
    )
    
    x_tran = length/2-padding
    y_tran = width /2-padding
    
    cut_cylinders = (
        cq.Workplane("XY")
        .add(cyl.translate((x_tran,y_tran,0)))
        .add(cyl.translate((-x_tran,y_tran,0)))
        
        .add(cyl.translate((x_tran,-y_tran,0)))
        .add(cyl.translate((-x_tran,-y_tran,0)))
    )
    
    cylinders = (
        cq.Workplane("XY")
        .add(cyl_i.translate((x_tran,y_tran,0)))
        .add(cyl_i.translate((-x_tran,y_tran,0)))
        
        .add(cyl_i.translate((x_tran,-y_tran,0)))
        .add(cyl_i.translate((-x_tran,-y_tran,0)))
    )
    
    result = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_cylinders)
        .union(cylinders)

    )
    return result
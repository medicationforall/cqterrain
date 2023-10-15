import cadquery as cq

def __add_shape(custom_shape, length, z_translate):
    def add_shape(loc):
        nonlocal custom_shape
        nonlocal length
        nonlocal z_translate
        return custom_shape.translate((length/2,0,z_translate/2)).val().located(loc)
    return add_shape

def spoked_wheel(
    radius = 10,
    height = 2,
    frame = 2,
    inner_radius = 3,
    spoke_width = 2,
    spoke_height = 1.5,
    spoke_fillet = .5,
    spoke_count = 12,
    frame_chamfer = .5,
    inner_chamfer = .5
):
    outline = cq.Workplane("XY").cylinder(height, radius)
    cut_cyl = cq.Workplane("XY").cylinder(height, radius-frame)
    inner_cyl = cq.Workplane("XY").cylinder(height, inner_radius)
    
    spoke_length = radius - frame - inner_radius
    spoke_z_translate = spoke_height - height
    spoke = (
        cq.Workplane("XY")
        .box(
            spoke_length+.2,
            spoke_width, 
            spoke_height
        )
    )
    
    if spoke_fillet:
        spoke = (
            spoke
            .faces("Z").edges("X")
            .fillet(spoke_fillet)
        )
    
    spokes =(
        cq.Workplane("XY")
        .polarArray(
            radius = inner_radius, 
            startAngle = 0, 
            angle = 360, 
            count = spoke_count,
            fill = True,
            rotate = True
        )
        .eachpoint(callback = __add_shape(
            spoke,
            spoke_length,
            spoke_z_translate
        ))
    )
    
    if frame_chamfer:
        outline = outline.faces("Z").edges().chamfer(frame_chamfer)
        
    if inner_chamfer:
        inner_cyl = inner_cyl.faces("Z").edges().chamfer(inner_chamfer)
    
    part = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_cyl)
        .union(inner_cyl)
        .union(spokes)
    )
    return part
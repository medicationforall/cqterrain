import cadquery as cq

def cap_greeble(
        diameter:float = 28, 
        teeth:int = 14,
        rotate_teeth:int = 20,
        body_height:float = 3,
        teeth_diameter:float = 3,
        chamfer:float = 2,
        interior_height:float = 2,
        interior_diameter:float = 4,
        interior_cut_diameter:float = 5,
        bars_count:int = 6,
        bar_length:float = 6,
        bar_diameter:float = 2,
        inset_distance:float = 2,
        bar_shift:float = 1,
        bar_shift_z:float = 2.4
    ):

    part = cq.Workplane("XY")
    body = cq.Workplane("XY").cylinder(body_height,diameter/2)
    
    cut = cq.Workplane("XY").cylinder(body_height,teeth_diameter/2).translate((diameter/2,0,0))
    cuts = cq.Workplane("XY")
    
    rotate_degrees = 360 / rotate_teeth
    for i in range(teeth):
        cuts = cuts.add(cut.rotate((0,0,1),(0,0,0),rotate_degrees*i))
        
    sub_body = (
        cq.Workplane("XY")
        .cylinder(body_height,diameter/2-inset_distance)
        .faces("Z")
        .chamfer(chamfer)
    )
    
    interior_cut = cq.Workplane("XY").cylinder(interior_height,diameter/2-interior_cut_diameter)
    interior_body = cq.Workplane("XY").cylinder(interior_height,interior_diameter)
    bar = cq.Workplane("XZ").cylinder(bar_length,bar_diameter).translate((0,bar_length/2+interior_diameter-bar_shift,bar_shift_z))
    bars = cq.Workplane("XY")
    
    rotate_degrees = 360 / bars_count
    for i in range(bars_count):
        bars = bars.add(bar.rotate((0,0,1),(0,0,0),rotate_degrees*i))
    
    part = part.union(body)
    part = part.cut(cuts)
    part = part.union(sub_body.translate((0,0,body_height)))
    part = part.cut(interior_cut.translate((0,0,body_height/2+interior_height)))
    part = part.union(interior_body.translate((0,0,body_height/2+interior_height)))
    part = part.union(bars)
    
    return part.translate((0,0,body_height/2))

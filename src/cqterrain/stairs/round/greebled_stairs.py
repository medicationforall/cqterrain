import cadquery as cq
import math

def greebled_stairs( 
    height:float = 71,
    inner_diameter:float = 76,
    diameter:float = 75+45,
    stair_height:float|None = 5.461538461538462,
    stair_count:int|None = None,
    inside_margin:float = 1.5,
    debug:bool = False
):
    cut_cylinder = cq.Workplane("XY").cylinder(height, inner_diameter/2)
    cut_cylinder_inside = cq.Workplane("XY").cylinder(height, (inner_diameter/2)+inside_margin)
    outline = cq.Workplane("XY").cylinder(height, diameter/2)
    intersect = cq.Workplane("XY").box(diameter,diameter,height)
    
    if stair_count is None and stair_height is not None:
        stair_count = math.floor(height / stair_height)
    elif stair_count is not None:
        stair_height = height / stair_count
    else:
        raise Exception('stair_count and stair_height are None')
    
    stair_deg = 90 / stair_count
    
    #outline
    stair_outline = cq.Workplane("XY").cylinder(stair_height, diameter/2)
    stair_inside_track = cq.Workplane("XY").cylinder(stair_height-inside_margin, (diameter/2)-inside_margin)
    
    stair_single = (
        cq.Workplane("XY")
        .union(stair_outline)
        .cut(cut_cylinder)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    )
    
    stair_inside = (
        cq.Workplane("XY")
        .union(stair_inside_track)
        .cut(cut_cylinder_inside)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    ).translate((0,0,-(inside_margin/2)))
    
    stair_single = stair_single.cut(stair_inside)
    
    #return 
    
    stair_rough = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_cylinder)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    )
    
    stairs = cq.Workplane("XY")
    
    for i in range(stair_count):
        #log(f"add stair {i}, {stair_deg*i}")
        stairs = stairs.translate((0,0,-stair_height*1)).union(stair_single.rotate((0,0,1),(0,0,0),-stair_deg*i))
        
    #return stair_single
    
    if debug:
        return stairs.translate((0,0,height/2-stair_height/2)).add(stair_rough)
    else:
        return stairs.translate((0,0,height/2-stair_height/2)).intersect(stair_rough)
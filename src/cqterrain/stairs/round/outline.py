import cadquery as cq


def outline(
    height:float = 71,
    inner_diameter:float = 76,
    diameter:float = 75+45,
    rotate:float = 40,
    debug:bool = False
):
    cut_cylinder = cq.Workplane("XY").cylinder(height, inner_diameter/2)
    outline = cq.Workplane("XY").cylinder(height, diameter/2)
    intersect = cq.Workplane("XY").box(diameter,diameter,height)
    
    stair_rough = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_cylinder)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    )
    
    if debug:
        return (
            stair_rough
            .add(stair_rough.rotate((0,0,1),(0,0,0),-rotate))
        ).translate((0,0,height/2))
    else:
        return (
            stair_rough
            .intersect(stair_rough.rotate((0,0,1),(0,0,0),-rotate))
        ).translate((0,0,height/2))
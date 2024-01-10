import cadquery as cq
import math

def _make_lines(
    length, 
    width, 
    height,
    line_width
):
    outline = cq.Workplane("XY").box(length, width, height)
    hyp = math.hypot(length, width)
    #log(hyp)
    
    angle = length/hyp
    angle_radians = math.acos((angle))
    angle_deg = math.degrees(angle_radians)
    #log(angle_deg)
    
    line = (
        cq.Workplane("XY")
        .box(hyp, line_width, height)
        
    )
    
    lines = (
        cq.Workplane("XY")
        .union(line.rotate((0,0,1),(0,0,0),angle_deg))
        .union(line.rotate((0,0,1),(0,0,0),-1*angle_deg))
    )
    return lines

def charge(
    length = 30, 
    width = 25, 
    height = 4,
    line_width = 3,
    line_depth = 1,
    corner_chamfer = 4,
    edge_chamfer = 2,
    padding = 2.5
):
    outline = cq.Workplane("XY").box(
        length, 
        width, 
        height
    )
    
    if corner_chamfer:
        outline = (
            outline
            .faces("X or -X")
            .edges("Z")
            .chamfer(corner_chamfer)
        )
        
    if edge_chamfer:
        outline = (
            outline
            .faces("Z")
            .chamfer(edge_chamfer)
        )
        
    lines = _make_lines(
        length-(edge_chamfer*2)-padding*2, 
        width-(edge_chamfer*2)-padding*2,
        line_depth,
        line_width, 
        
    )
    
    charge_tile = (
        cq.Workplane("XY")
        .union(outline)
        .cut(lines.translate((0,0,height/2-line_depth/2)))
    )
    
    return charge_tile
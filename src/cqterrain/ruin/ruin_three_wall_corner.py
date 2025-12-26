import cadquery as cq
from . import ruin_corner

def ruin_three_wall_corner(
        length:float = 50, 
        width:float = 50, 
        height:float = 50, 
        wall_width:float = 5,
        base_points:int = 5,
        base_adjustments:list[tuple[float,float]] = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
        x_points:int = 3,
        x_adjustments:list[tuple[float,float]] = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
        y_points:int = 4,
        y_adjustments:list[tuple[float,float]] = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)]
):
    ex_base = ruin_corner(
        length=length, 
        width = width, 
        height = wall_width,
        points = base_points,
        adjustments = base_adjustments
    )
    ex_wall_one = (
        ruin_corner(
            length=length, 
            width = height, 
            height = wall_width,
            points = x_points,
            adjustments = x_adjustments
        )
        .translate((0,0,-wall_width))
        .rotate((1,0,0),(0,0,0),-90)
    )
    
    ex_wall_two = (
        ruin_corner(
            length=width, 
            width = height, 
            height = wall_width,
            points = y_points,
            adjustments = y_adjustments
        ).translate((0,0,0))
        .rotate((1,0,0),(0,0,0),-90)
        .rotate((0,0,1),(0,0,0),-90)
    )
    
    strut_one = cq.Workplane("XY").add(ex_base).intersect(ex_wall_one)
    strut_two = cq.Workplane("XY").add(ex_base).intersect(ex_wall_two)
    strut_three = cq.Workplane("XY").add(ex_wall_one).intersect(ex_wall_two)
    
    struts = (
        cq.Workplane("XY").union(strut_one).union(strut_two)
        .union(strut_three))
    
    c_strut_one = cq.Workplane("XY").box(length,wall_width,wall_width)
    c_strut_two = cq.Workplane("XY").box(width,wall_width,wall_width)
    c_strut_three = cq.Workplane("XY").box(height,wall_width,wall_width)
    
    cut_corners = (
        cq.Workplane("XY")
        .union(
            c_strut_one
            .translate((length/2,wall_width/2,wall_width/2))
        )
        .union(
            c_strut_two
            .translate((width/2,-wall_width/2,wall_width/2))
            .rotate((0,0,1),(0,0,0),-90)
        )
        .union(
            c_strut_three
            .translate((height/2,wall_width/2,-wall_width/2))
            .rotate((0,1,0),(0,0,0),90)
        )
        .cut(struts)
    )
    
    ruin = (
        cq.Workplane("XY")
        .union(ex_base)
        .union(ex_wall_one)
        .union(ex_wall_two)
    )
    
    corner_combined = ruin.cut(cut_corners)
    return corner_combined
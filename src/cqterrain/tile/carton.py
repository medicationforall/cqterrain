import cadquery as cq

def _carton_line(
    length=30, 
    width=25, 
    line_width = 2,
    line_depth = 1,
    x_divisor = 3,
    y_divisor = 2
):
    pts = [
        (0,0),
        (0,line_width),
        (length/x_divisor-line_width/2,line_width),
        (length/x_divisor+length/x_divisor,width/y_divisor), 
        (length,width/y_divisor),
        (length,width/y_divisor-line_width),
        (length/x_divisor+length/x_divisor+line_width/2,width/y_divisor-line_width),
        (length/x_divisor,line_width-line_width),
    ]
    
    cut_line = (
        cq.Workplane("XY")
        .polyline(pts)
        .close()
        .extrude(line_depth)
    ).translate((-1*(length/2),-1*(width/(y_divisor*2)),-1*(line_depth/2)))
    return cut_line

def carton(
        length=30, 
        width=25, 
        height = 4,
        line_width = 2,
        line_depth = 1,
        x_divisor = 3,
        y_divisor = 3
):
    cut_line = _carton_line(
        length, 
        width, 
        line_width, 
        line_depth, 
        x_divisor,
        y_divisor
    )
    outline = cq.Workplane("XY").box(length, width, height)    
    cut_end = cq.Workplane("XY").box(line_depth,line_width,height)
    
    carton_tile = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_line.translate((0,0,height/2 - line_depth/2)))
        .cut(cut_end.translate((length/2-line_depth/2,width/(y_divisor*2)-line_width/2,0)))
        .cut(cut_end.translate((-1*(length/2-line_depth/2),-1*(width/(y_divisor*2)-line_width/2),0)))
    )
    return carton_tile
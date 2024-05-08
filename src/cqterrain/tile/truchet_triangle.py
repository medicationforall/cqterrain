import cadquery as cq

def truchet_triangle(
        length:float = 10, 
        width:float = 10, 
        height:float = 4, 
        min_height:float = 2
    ) -> cq.Workplane:
    
    base = cq.Workplane("XY").box(length, width, min_height).translate((0,0,-(min_height/2)))
    pts = [(0,0),(length,0),(length,width)]
    triangle = (cq.Workplane("XY").center(-length/2,-width/2).polyline(pts).close().extrude(height-min_height))
    
    return base.union(triangle).translate((0,0,min_height)).translate((0,0,-(height/2)))


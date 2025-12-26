import cadquery as cq

def corner(
    length:float = 50, 
    width:float = 50, 
    height:float = 5
):
    pts = [(0,0),(0,width),(length,0)]
    
    ruin = (
        cq.Workplane("XY")
        .polyline(pts)
        .close()
    )
    
    if height:
        ruin = ruin.extrude(height)
    
    return ruin
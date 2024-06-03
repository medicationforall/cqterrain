import cadquery as cq

def hip(
        length:float = 40, 
        width:float = 40, 
        top:float = 0, 
        left:float = 0, 
        right:float = 0, 
        height:float = 40
    ) -> cq.Workplane:
    top_r = top / 2
    max_w = width / 2
    max_l = length / 2

    roof = (
        cq.Workplane("XY")
        .wedge(
            length,
            height,
            width,
            max_l - top_r - left,
            max_w - top_r,
            max_l + top_r + right,
            max_w + top_r
        )
        .rotate((1,0,0), (0,0,0), -90)
    )
    return roof
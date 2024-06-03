import cadquery as cq

def gable(
        length:float = 40, 
        width:float = 40, 
        height:float = 40
    ) -> cq.Workplane:
    roof = (
        cq.Workplane("XY" )
        .wedge(
            length,
            height,
            width,
            0,
            0,
            length,
            0
        )
        .rotate((1,0,0), (0,0,0), -90)
    )
    return roof

def dollhouse_gable(
        length:float = 40, 
        width:float = 40, 
        height:float = 40
    ) -> cq.Workplane:
    print("Deprecated us gable instead")
    return gable(length, width, height)

import cadquery as cq

def shell(
        part:cq.Workplane, 
        face:str = "-Z", 
        width:float=-1
    )->cq.Workplane:
    result = part.faces(face).shell(width)
    return result
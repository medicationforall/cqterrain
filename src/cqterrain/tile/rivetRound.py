import cadquery as cq

def __add_shape(custom_shape, padding=0, height=0, rivet_height =2):
    def add_shape(loc):
        nonlocal custom_shape
        nonlocal padding
        nonlocal height
        nonlocal rivet_height
        return custom_shape.translate((-2,0,height/2+rivet_height/2)).val().located(loc)
    return add_shape

def rivet_round(
        radius = 10, 
        height = 2,
        rivet_height = 0.5,
        rivet_radius = .5,
        padding = 1,
        rivet_count = 5
):
    base = cq.Workplane("XY").cylinder(height, radius)
    rivet = cq.Workplane("XY").cylinder(rivet_height, rivet_radius)
    rivets =(
        cq.Workplane("XY")
        .polarArray(
            radius = radius, 
            startAngle = 0, 
            angle = 360, 
            count = rivet_count,
            fill = True,
            rotate = True
        )
        .eachpoint(callback = __add_shape(
            rivet, 
            padding, 
            height, 
            rivet_height
        ))
    )
    return base.union(rivets)
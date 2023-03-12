import cadquery as cq
import math

def __points_extrude_faces(
        points=[(0,0),(0,12.5),(2,12.5) ,(4,4), (4,0)],
        extrude=10,
        faces=4,
        intersect=True
    ):
    poly = (
        cq.Workplane("XY")
        .polyline(points).close()
        .extrude(extrude)
        .translate((0,0,-1*(extrude/2)))
    )

    mirror = (
        cq.Workplane("XY")
        .union(poly)
        .union(poly.rotate((1,0,0),(0,0,0),180))
    )

    rotate_degrees = math.floor(360 / faces)
    rotations = int(faces/2)

    scene = (
        cq.Workplane("XY")
        .union(mirror)
    )
    for i in range(rotations):
        if i == 0:
            scene = scene.union(mirror)
        else:
            if intersect:
                scene = scene.intersect(mirror.rotate((1,0,0),(0,0,0),rotate_degrees*i))
            else:
                scene = scene.union(mirror.rotate((1,0,0),(0,0,0),rotate_degrees*i))

    return scene.rotate((0,1,0),(0,0,0),90)

def obelisk(
        base_width=30,
        base_height=3,
        inset_width=15,
        inset_height=5,
        mid_width=30,
        mid_height=15,
        top_width=15,
        top_height=70,
        height=102,
        faces=4,
        intersect=True
        ):
    in_height = base_height + inset_height
    mid_height = in_height + mid_height
    t_height = mid_height + top_height

    points=[
        (0,0),
        (0,base_width/2),
        (base_height, base_width/2),
        (in_height,inset_width/2),
        (mid_height, mid_width/2),
        (t_height, top_width/2),
        (height,0)
    ]

    extrude = base_width
    extrude = inset_width if inset_width > extrude else extrude
    extrude = mid_width if mid_width > extrude else extrude
    extrude = top_width if top_width > extrude else extrude

    return (
        __points_extrude_faces(points, extrude, faces, intersect)
        .translate((0,0,-1*(height/2)))
    )

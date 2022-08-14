import cadquery as cq
from cqterrain import floor, wall

def make_room(length=50, width=100, height=50):
    print('make room')
    # make floor
    r_floor = floor.make_floor(length, width)
    r_height = r_floor.metadata['height']
    r_width = r_floor.metadata['width']
    r_length = r_floor.metadata['width']
    # make walls
    w1 = wall.make_wall()
    w1_height = w1.metadata['height']
    w1_width = w1.metadata['width']

    w2 = wall.make_wall()
    w2_height = w2.metadata['height']
    w2_width = w2.metadata['width']

    w3 = wall.make_wall()
    w3_height = w3.metadata['height']
    w3_width = w3.metadata['width']
    w3_rotated = w3.rotate((0, 0, 1), (0, 0, 0), -90)

    w4 = wall.make_wall()
    w4_height = w4.metadata['height']
    w4_width = w4.metadata['width']
    w4_rotated = w4.rotate((0, 0, 1), (0, 0, 0), -90)

    room_assembly = cq.Assembly()
    room_assembly.add(r_floor, name="floor")
    room_assembly.add(w1, name="wall1", loc=cq.Location(cq.Vector(0, (r_width /2) - (w1_width /2), (w1_height /2)-(r_height/2))))
    room_assembly.add(w2, name="wall2", loc=cq.Location(cq.Vector(0, -1*((r_width /2) - (w1_width /2)), (w2_height /2)-(r_height/2))))
    room_assembly.add(w3_rotated, name="wall3", loc=cq.Location(cq.Vector((r_length /2) - (w1_width /2), 0, (w2_height /2)-(r_height/2))))
    room_assembly.add(w4_rotated, name="wall4", loc=cq.Location(cq.Vector(-1*((r_length /2) - (w1_width /2)), 0, (w2_height /2)-(r_height/2))))
    comp_room = room_assembly.toCompound()

    return comp_room

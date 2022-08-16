import cadquery as cq
from cqterrain import floor, wall

def make_room(length=120, width=80, height=50, wall_width=3, floor_height=3, floor_padding=0):
    # make floor
    r_floor, r_height, r_width, r_length = __make_floor(length, width, height=floor_height, padding=floor_padding)

    # make walls along the x axis
    w1, w1_height, w1_width = __make_wall(length=r_length, width=wall_width, height=height)
    w2, w2_height, w2_width = __make_wall(length=r_length, width=wall_width, height=height)

    # walls along the y axis
    w3, w3_height, w3_width = __make_wall(length=r_width, width=wall_width, height=height)
    w3_rotated = w3.rotate((0, 0, 1), (0, 0, 0), -90)

    w4, w4_height, w4_width = __make_wall(length=r_width, width=wall_width, height=height)
    w4_rotated = w4.rotate((0, 0, 1), (0, 0, 0), -90)

    room_assembly = cq.Assembly()
    room_assembly.add(r_floor, name="floor")
    room_assembly.add(w1, name="wall1", loc=cq.Location(cq.Vector(0, (r_width /2) - (w1_width /2), (w1_height /2)-(r_height/2))))
    room_assembly.add(w2, name="wall2", loc=cq.Location(cq.Vector(0, -1*((r_width /2) - (w1_width /2)), (w2_height /2)-(r_height/2))))
    room_assembly.add(w3_rotated, name="wall3", loc=cq.Location(cq.Vector((r_length /2) - (w1_width /2), 0, (w2_height /2)-(r_height/2))))
    room_assembly.add(w4_rotated, name="wall4", loc=cq.Location(cq.Vector(-1*((r_length /2) - (w1_width /2)), 0, (w2_height /2)-(r_height/2))))
    comp_room = room_assembly.toCompound()

    # zero out height
    comp_room = comp_room.translate((0,0, floor_height/2))
    comp_room = comp_room.translate((0,0, -1*(height/2)))

    return comp_room

def __make_floor(length, width, height, padding):
    padding = padding*2
    r_floor = floor.make_floor(length, width, height)
    r_height = r_floor.metadata['height']
    r_width = r_floor.metadata['width'] - padding
    r_length = r_floor.metadata['length'] - padding
    return r_floor, r_height, r_width, r_length

def __make_wall(length, width, height):
    w = wall.make_wall(length, width, height)
    w_height = w.metadata['height']
    w_width = w.metadata['width']
    return w, w_height, w_width

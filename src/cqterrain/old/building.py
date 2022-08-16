import cadquery as cq
from cadqueryhelper import shape
from cqterrain import room

def make_building(length=100, width=100, height=300, stories=3):
    print('make building')
    room_height = height/stories

    building_assembly = cq.Assembly()

    # could be a series
    for i in range(stories):
        floor = room.make_room(length, width, height=room_height)
        print('after', room_height)
        building_assembly.add(floor, name=f"story{i}", loc=cq.Location(cq.Vector(0, 0, i*room_height)))


    comp_building = building_assembly.toCompound()
    return comp_building

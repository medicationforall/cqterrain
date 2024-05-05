import cadquery as cq
from cqterrain import Building

building = Building(
    length=50,
    width=60,
    height=100,
    stories=4
)

building.room['wall_width'] = 4
building.room['floor_height'] = 5
building.room['floor_padding'] = 1

building.has_stairs = True
building.stair['rail_height'] = 5
#building.stair['width'] = 15
#building.stair['run'] = 10

#building.stories = 2
building.make()


#room_replace = room.make_room(length=100, width=120)
#building.floors[1] = room_replace


ex = building.build()
workspace = cq.Workplane('XY')
workspace.add(ex)

#show_object(ex)
cq.exporters.export(workspace,'stl/building.stl')
#assemble.save('gltf/building.gltf', exportType='GLTF')
#cq.exporters.export(workspace,'gltf/building.gltf', exportType='GLTF')


import cadquery as cq
from cqterrain.building import Building

b = Building(height=200, width=90, length=100, has_stairs=True, stories=4)
b.room["window_count"]=5
b.room["floor_padding"]=5
b.room["style"]="arch"
b.stair_stories = 2
b.make()

ground_floor = b.floors[0]
ground_floor.floor_padding=2
ground_floor.style="office"
ground_floor.door_walls=[False, False, False, True]
ground_floor.window_walls=[False, True, True, True]
ground_floor.door["x_offset"]=-25
ground_floor.door["height"] = 35
ground_floor.window_count = 2
ground_floor.make()

second_floor = b.floors[1]
second_floor.window_walls=[True, True, False, True]
second_floor.make()

third_floor = b.floors[2]
third_floor.window_walls=[True, False, True, True]
third_floor.door_walls=[False, True, False, False]
third_floor.door["x_offset"]=27
third_floor.window_count=4
third_floor.make()

building = b.build()
#show_object(building.translate((0,0,25)))

#hacked roof
roof = cq.Workplane("XY").wedge(100, 40, 100, 20, 50, 80, 50)
#show_object(roof.rotate((1,0,0), (0,0,0), -90).translate((00,0,20+200)))

#hacked balcony
balcony = cq.Workplane().box(50, 10, 3)
#show_object(balcony.translate((35,-50,1.5+100)))

#hacked stair connector
balcony2 = cq.Workplane().box(10, 10, 5)
#show_object(balcony2.translate((55,50,2.5+50)))

scene = (cq.Workplane("XY")
.add(building.translate((0,0,25)))
.add(roof.rotate((1,0,0), (0,0,0), -90).translate((00,0,20+200)))
.add(balcony.translate((35,-50,1.5+100)))
.add(balcony2.translate((55,50,2.5+50)))
)

cq.exporters.export(scene,'stl/building_with_roof.stl')

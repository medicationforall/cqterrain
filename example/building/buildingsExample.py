import cadquery as cq
from cadqueryhelper import series, shape
from cqterrain.building import Room, Building

ex = Room(
    length=104,
    width=79,
    height=30,
    wall_width=4,
    floor_height=3,
    floor_padding=2,
    window_count = 2
)


ex.make()
room = ex.build()

bb = Building(
    length=60,
    width=70,
    height=120,
    stories=4
    )
bb.room['wall_width'] = 4
bb.room['floor_height'] = 5
bb.room['floor_padding'] = 1

bb.has_stairs = True
bb.stair['rail_height'] = 5

bb.make()
building = bb.build()


bb2 = Building(
    length=60,
    width=70,
    height=150,
    stories=5,
    )
bb2.room['wall_width'] = 4
bb2.room['floor_height'] = 5
bb2.room['floor_padding'] = 1
bb2.room['style'] = 'arch'
bb2.room['window_count'] = 3

bb2.has_stairs = True
bb2.stair['rail_height'] = 5

bb2.make()
building2 = bb2.build()

width=5
window_count=2
window_ridge = shape.arch_pointed(length=12, width=width+2, height=22, inner_height=11)
window_cutout2 = shape.arch_pointed(length=10, width=width+2, height=20, inner_height=10)
window = window_ridge.cut(window_cutout2)
window_series2 = series(window, window_count, length_offset = 1)

scene = (cq.Workplane("XY")
         .add(room.translate((0, 90, 0)))
         .add(building)
         .add(building2.rotate((0,0,1),(0,0,0),90).translate((100,0,0)))
         )

cq.exporters.export(scene,'stl/buildingsExample.stl')

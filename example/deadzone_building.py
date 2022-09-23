import cadquery as cq
from cqterrain import Building, Room, tile

render_floor = True
cq_editor_show=True
export_to_file=False

floor_tile = tile.octagon_with_dots()

def make_entrance():
    bp = Building(length=75, width=75, height=75, stories=1, has_stairs=True)
    bp.stair_stories = 1
    bp.room['build_walls']= [True,False,True,True]
    bp.room['door_walls'] = [False, False, True, False]
    bp.room['window_walls'] = [True, False, False, False]
    if render_floor:
        bp.room['floor_tile'] = floor_tile
        bp.room['floor_tile_padding'] = 0.5
    bp.window['count'] = 2

    bp.stair['length_padding'] = 25
    bp.stair['width']=25
    bp.stair['start_rotation']=-90
    bp.stair['direction']='clockwise'
    bp.stair_landing['width'] = 25
    bp.stair_landing['length'] = 25

    bp.make()
    bp.stairs[0] = bp.stairs[0].translate((0,12.5,0))
    bp.floors[0].window['padding'] = 5
    bp.floors[0].window['height'] = 35
    bp.floors[0].window['length'] = 20
    bp.floors[0].door['length']=35
    bp.floors[0].make()

    entrance = bp.build().translate((0,75,0))
    return entrance

def make_roof(height=20):
    bp = Room(
        length=75,
        width=75,
        height=height,
        build_walls = [True, False, True, True],
        window_walls = [False, False, False, False],
        door_walls = [False, False, False, False],
        )
    bp.make()
    roof = bp.build()
    roof = roof.translate((0,75,10+37.5))
    return roof


def make_tower():
    bp = Building(length=75, width=75, height=150, stories=2)
    bp.room['build_walls']= [True,True,True,False]
    bp.room['door_walls'] = [True, False, False, False]
    bp.room['window_walls'] = [False, True, True, False]
    if render_floor:
        bp.room['floor_tile'] = floor_tile
        bp.room['floor_tile_padding'] = 0.5
    bp.window['count'] = 3
    bp.window['padding'] = 3
    bp.window['height'] = 25
    bp.window['length'] = 18
    bp.make()
    bp.floors[0].door['length']=35
    bp.floors[0].make()
    bp.floors[1].door['length']=35
    bp.floors[1].make()
    building = bp.build()
    return building

def make_tower2():
    bp = Building(length=75, width=75, height=150, stories=2)
    bp.room['build_walls']= [True,True,False,True]
    if render_floor:
        bp.room['floor_tile'] = floor_tile
        bp.room['floor_tile_padding'] = 0.5
    bp.window['count'] = 3
    bp.window['padding'] = 4
    bp.window['padding'] = 3
    bp.window['height'] = 25
    bp.window['length'] = 18
    bp.make()

    bp.floors[0]
    bp.floors[0].door_walls = [False, False, False, True]
    bp.floors[0].window_walls = [True, True, False, False]
    bp.floors[0].door['length']=35
    bp.floors[0].make()

    building = bp.build()
    building  = building.translate((-75,0,0))
    return building

tower = make_tower()
tower1_roof = make_roof(10).translate((0,-75,70)).rotate((0,0,1),(0,0,0),90)
tower= cq.Workplane("XY").add(tower).add(tower1_roof)

tower2 = make_tower2()
tower2_roof = make_roof(height=10).translate((0,0,70)).rotate((0,0,1),(0,0,0),-90)
tower2= cq.Workplane("XY").add(tower2).add(tower2_roof)

entrance = make_entrance()
entrance_roof = make_roof()
entrance= cq.Workplane("XY").add(entrance).add(entrance_roof)

scene = (cq.Workplane("XY")
         .add(tower)
         .add(tower2)
         .add(entrance)
         )




mini = cq.Workplane("XY" ).cylinder(32, 12.5).translate((-10,70,(32/2)-37.5+78))

if cq_editor_show:
    show_object(mini)
    show_object(scene)

if export_to_file:
    cq.exporters.export(scene,'out/deadzone_building.stl')


#show_object(combined)

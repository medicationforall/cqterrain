import cadquery as cq
from cadqueryhelper import series, shape
from cqterrain import Building, Room, tile

render_floor = True
cq_editor_show = False
export_to_file = True

create = ['tower1', 'tower2', 'entrance']
create = [ 'entrance']

floor_tile = tile.octagon_with_dots()

def _make_window(length, width, height):
    frame = cq.Workplane("XY").box(length, width+2, height)
    window = cq.Workplane("XY").box(length-8, width+2, height)
    combined = frame.cut(window)

    top_spheres = combined.edges("X").translate((0,0,-2)).sphere(1, combine=False)
    bottom_spheres = combined.edges("X").translate((0,0,2)).sphere(1, combine=False)

    combined = combined.edges("X").chamfer(.7).cut(top_spheres).cut(bottom_spheres)
    return combined

def custom_windows(wall, length, width, height, count, padding):
    window_cutout = cq.Workplane().box(length, width, height)
    window_cut_series = series(window_cutout, count, length_offset = padding)

    window = _make_window(length, width, height)
    window_series = series(window, count, length_offset = padding)

    w = wall.cut(window_cut_series)
    w = w.add(window_series)

    return w

def make_entrance():
    bp = Building(length=75, width=75, height=75, stories=1, has_stairs=True)
    bp.stair_stories = 1
    bp.room['build_walls']= [True,False,True,True]
    bp.room['door_walls'] = [False, False, True, False]
    bp.room['window_walls'] = [True, False, False, False]
    if render_floor:
        bp.room['floor_tile'] = floor_tile
        bp.room['floor_tile_padding'] = .5
    bp.window['count'] = 2
    bp.room['make_custom_windows'] = custom_windows

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

    for index, wall in enumerate(bp.walls):
        bp.walls[index] = wall.chamfer(1)

    roof = bp.build()
    roof = roof.translate((0,75,10+37.5))
    return roof


def make_tower():
    bp = Building(length=75, width=75, height=150, stories=2)
    bp.room['build_walls']= [True,True,True,False]
    bp.room['door_walls'] = [True, False, False, False]
    bp.room['window_walls'] = [False, True, True, False]
    bp.room['make_custom_windows'] = custom_windows
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
    bp.room['make_custom_windows'] = custom_windows
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

scene = cq.Workplane("XY")

if 'tower1' in create:
    tower = make_tower()
    tower1_roof = make_roof(10).translate((0,-75,70)).rotate((0,0,1),(0,0,0),90)
    tower= cq.Workplane("XY").add(tower).add(tower1_roof)
    scene.add(tower)

if 'tower2' in create:
    tower2 = make_tower2()
    tower2_roof = make_roof(height=10).translate((0,0,70)).rotate((0,0,1),(0,0,0),-90)
    tower2= cq.Workplane("XY").add(tower2).add(tower2_roof)
    scene.add(tower2)

if 'entrance' in create:
    entrance = make_entrance()
    entrance_roof = make_roof()

    entrance= cq.Workplane("XY").add(entrance).add(entrance_roof)
    scene.add(entrance)



mini = cq.Workplane("XY" ).cylinder(32, 12.5).translate((-10,70,(32/2)-37.5+78))

if cq_editor_show:
    show_object(mini)
    show_object(scene)

if export_to_file:
    cq.exporters.export(scene,'out/deadzone_building.stl')

#window = _make_window(20,5, 20)
#show_object(window)

import cadquery as cq
from cadqueryhelper import series, shape
from cqterrain.building import Building, Room
from cqterrain import tile, window
from cqterrain.door import TiledDoor

render_floor = False
cq_editor_show=False
export_to_file=True

create = ['tower1', 'tower2', 'entrance']
#create = [ 'entrance']

floor_tile = tile.octagon_with_dots()

def custom_windows(
        wall, 
        length, 
        width, 
        height, 
        count, 
        padding
    ):
    window_cutout = cq.Workplane().box(length, width, height)
    window_cut_series = series(window_cutout, count, length_offset = padding)

    i_window = window.industrial(length, width+2, height)
    grill = window.grill(length=20, height=60, rows=2, columns=2)
    i_window.add(grill)
    window_series = series(i_window, count, length_offset = padding)

    w = wall.cut(window_cut_series)
    w = w.add(window_series)

    return w

def make_custom_door(wall, length, width, height, floor_height):
    bottom = wall.faces("-Z").val()
    cutout = (
        cq.Workplane(bottom.Center())
        .box(length, width, height)
        .translate((0,0,(height/2)+floor_height))
    )
    
    door_bp = TiledDoor()
    door_bp.length = length
    door_bp.width = width-.5
    door_bp.height = height
    door_bp.make()
    door_instance = door_bp.build()
    
    def add_door(loc: cq.Location) -> cq.Shape:
        return door_instance.translate((0,0,(height/2)+floor_height)).val().located(loc) #type: ignore
        
        
    door_wrapper = cq.Workplane(bottom.Center()).eachpoint(callback = add_door)

    #log(bottom.Center())
    wall = wall.cut(cutout).union(door_wrapper)
    #new_wall = cq.Workplane("XY").box(length, width, height)
    return wall

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
    bp.room['make_custom_door'] = make_custom_door

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
    bp.room['make_custom_door'] = make_custom_door
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
    bp.room['make_custom_door'] = make_custom_door
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

if 'entrance' in create:
    entrance = make_entrance()
    entrance_roof = make_roof()
    stair_cutout = cq.Workplane("XY").box(4, 30, 20).translate((-37.5+1.5,37.5+12.5+1,37.5+10+3))
    entrance= (cq.Workplane("XY")
               .add(entrance)
               .add(entrance_roof)
               )
    scene = scene.union(entrance).cut(stair_cutout)

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


mini = cq.Workplane("XY" ).cylinder(32, 12.5).translate((-10,70,(32/2)-37.5+78))

if cq_editor_show:
    show_object(mini)
    show_object(scene)

if export_to_file:
    cq.exporters.export(scene,'stl/building_deadzone.stl')

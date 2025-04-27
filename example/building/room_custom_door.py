import cadquery as cq
from  cqterrain.building  import Room
from cqterrain.door import TiledDoor 

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
        
        
    door_wrapper = cq.Workplane(bottom.Center()).eachpoint(add_door)

    #log(bottom.Center())
    wall = wall.cut(cutout).union(door_wrapper)
    #new_wall = cq.Workplane("XY").box(length, width, height)
    return wall

bp_room = Room()
bp_room.length= 120
bp_room.width = 80
bp_room.height= 50
bp_room.wall_width = 3
bp_room.floor_height = 3
bp_room.floor_padding = 0
bp_room.floor_tile = None
bp_room.floor_tile_padding = 0
bp_room.style = "office"
bp_room.window_count= 1
bp_room.door_walls = [False, True, False, False]
bp_room.window_walls = [True, False, True, True]
bp_room.build_walls = [True, True, True, True]
bp_room.make_custom_door = make_custom_door
bp_room.door['width'] = 3

bp_room.make()
result = bp_room.build()

#show_object(result)
cq.exporters.export(result,'stl/building_room_custom_door.stl')
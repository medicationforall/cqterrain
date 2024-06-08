## Door
### parameters
* length: float 
* width: float 
* frame_length: float 
* frame_height: float 
* inner_width: float 
* height: float 
* x_offset: float

``` python
    bp_door = Door()
    bp_door.length = 25
    bp_door.width = 8
    bp_door.frame_length = 3 
    bp_door.frame_height = 4
    bp_door.inner_width = 3
    bp_door.height  = 40
    bp_door.x_offset = 0

    bp_door.make()
    result = bp_door.build()
```

![](image/door/01.png)

* [source](../src/cqterrain/door/Door.py)
* [example](../example/door/door.py)
* [stl](../stl/door.stl)

## Pull Handle

### parameters
* length: float 
* width: float 
* height: float
* handle_length: float
* handle_width_padding: float
* handle_z_margin: float
* handle_base_chamfer: float
* mirrored: bool

``` python
import cadquery as cq
from cqterrain.door import pull_handle

handle_ex = pull_handle(
    length = 3, 
    width = 4, 
    height = 6,
    handle_length = 1,
    handle_width_padding = 1,
    handle_z_margin = 2,
    handle_base_chamfer = 1,
    mirrored = False
)
```

![](image/door/02.png)

* [source](../src/cqterrain/door/pull_handle.py)
* [example](../example/door/pull_handle.py)
* [stl](../stl/pull_handle.stl)

## Tiled Door

### parameters
length:float = 30
width:float = 3
height:float = 40

render_tiles=True
tiles_x_count:int = 2
tiles_y_count:int = 3
tile_x_padding:float = 3
tile_y_padding:float = 2
tile_width_padding:float = .5

render_handle:bool=True
handle_length:float
handle_width_padding:float
handle_height:float
handle_x_margin:float

## method callbacks
* tile_bp: Callable[[float, float, float], cq.Workplane]
* handle_bp: Callable[[float, float, float], cq.Workplane]

``` python
import cadquery as cq
from cqterrain.door import TiledDoor

door_bp = TiledDoor()
door_bp.length = 30
door_bp.width = 3
door_bp.height = 45

door_bp.render_tiles = True
door_bp.tiles_x_count = 2
door_bp.tiles_y_count = 3
door_bp.tile_x_padding = 3
door_bp.tile_y_padding = 1
door_bp.tile_width_padding = .5

door_bp.render_handle = True
door_bp.handle_length = 3
door_bp.handle_height = 6
door_bp.handle_x_margin = .5

door_bp.make()

door_ex = door_bp.build()
```

![](image/door/03.png)

* [source](../src/cqterrain/door/TiledDoor.py)
* [example](../example/door/tiled_door.py)
* [stl](../stl/door_tiled_door.stl)
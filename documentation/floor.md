# Floor

- [Floor](#floor)
  - [Round Brick Floor](#round-brick-floor)
    - [Parameters](#parameters)
    - [Advanced Example](#advanced-example)
  - [Wood Floor Struct](#wood-floor-struct)
    - [Parameters](#parameters-1)
    - [Wood Floor example](#wood-floor-example)

---

## Round Brick Floor

Round Brick / Stone Pattern

### Parameters
* diameter:float
* height:float
* rows:int
* block_count:int
* ring_spacing:float
* spacer_width:float
* ring_skip_index:int|None
  
``` python
import cadquery as cq
from cqterrain.floor import RoundBrickFloor

bp_floor = RoundBrickFloor()
bp_floor.diameter = 100
bp_floor.height = 4
bp_floor.block_count = 8
bp_floor.rows = 10
bp_floor.ring_spacing = 1.5
bp_floor.spacer_width = 1

bp_floor.ring_skip_index = None
bp_floor.make()

ex_floor = bp_floor.build()
show_object(ex_floor)
```

![](image/floor/01.png)<br />

* [source](../src/cqterrain/floor/RoundBrickFloor.py)
* [example](../example/floor/round_brick_floor.py)
* [stl](../stl/floor_roundBrickFloor.stl)

### Advanced Example
This example joins two RoundBrickFloor instances together to make a more dense brick pattern.

``` python
import cadquery as cq
from cqterrain.floor import RoundBrickFloor

bp_floor = RoundBrickFloor()
bp_floor.diameter = 50
bp_floor.block_count = 15
bp_floor.rows = 5
bp_floor.ring_skip_index = None
bp_floor.make()

ex_floor = bp_floor.build()

bp_floor_two = RoundBrickFloor()
bp_floor_two.ring_skip_index = 5
bp_floor_two.block_count = 24
bp_floor_two.make()

ex_floor_two = bp_floor_two.build()

combined = ex_floor.union(ex_floor_two)

show_object(combined)
```

![](image/floor/02.png)<br />

* [example](../example/floor/round_brick_floor_alt.py)
* [stl](../stl/floor_roundBrickFloor_alt.stl)


---

## Wood Floor Struct

### Parameters
* length: float
* width: float
* height: float
* joist_width: float
* joist_space: float
* joist_count: float
* render_joists: bool
* board_width: float
* board_width_spacer: float
* board_height: float
* nail_diameter: float
* nail_overlap_height: float
* nail_x_margin: float
* nail_y_margin: float
* seed: str
* board_lenghs: list[int]
* board_break_width: float
* grid: list[str]

``` python
import cadquery as cq
from cqterrain.floor import WoodFloor

bp_floor = WoodFloor()
bp_floor.length= 150
bp_floor.width= 75
bp_floor.height = 8

#joist
bp_floor.joist_width = 3
bp_floor.joist_space = 12.5
bp_floor.joist_count= 7
bp_floor.render_joists= True

# Board
bp_floor.board_width= 5
bp_floor.board_width_spacer = .1
bp_floor.board_height = 1.5

#nail
bp_floor.nail_diameter = .4
bp_floor.nail_overlap_height = .2
bp_floor.nail_x_margin = .5
bp_floor.nail_y_margin = .5

# grid
bp_floor.seed= "redd2"
bp_floor.board_lenghs = [1,4]
bp_floor.board_break_width= .2
bp_floor.grid = []

bp_floor.make()

ex_floor = bp_floor.build()

show_object(ex_floor)
```

![](image/floor/03.png)<br />

* [source](../src/cqterrain/floor/WoodFloor.py)
* [example](../example/floor/wood_floor_struct.py)
* [stl](../stl/floor_woodfloor_struct.stl)

### Wood Floor example

``` python
import cadquery as cq
from cqterrain.floor import WoodFloor

bp_floor = WoodFloor()
bp_floor.board_width = 5
bp_floor.render_joists = False
bp_floor.make()

ex_floor = bp_floor.build()

show_object(ex_floor)
```

![](image/floor/04.png)<br />

* [example](../example/floor/wood_floor.py)
* [stl](../stl/floor_woodfloor.stl)

---




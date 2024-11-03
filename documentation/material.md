# Material
## make_stones

Create a sparse pattern of the given parts. 
This method of generation should be relatively performant.

### parameters
* parts: list[cq.Workplane]
* dim: list[float]
* rows: int
* columns: int
* seed: str

``` python
import cadquery as cq
from cqterrain.material import make_stones


tile = cq.Workplane("XY").box(5,5,2).chamfer(0.8)
tile2 = cq.Workplane("XY").box(4,4,2).fillet(.5)
tile3 = cq.Workplane("XY").box(3,6,2).chamfer(0.5)
tiles = make_stones(
    [
        tile, 
        tile2, 
        tile3
    ], 
    [6,6,2], 
    columns = 10, 
    rows = 3,
    seed = "test4"
)

show_object(tiles)
```

![](image/stone/01.png)

* [source](../src/cqterrain/material/stone.py)
* [example](../example/material/stones.py)
* [stl](../stl/material_stones.stl)

---

## uneven_blocks

### paramaters
* tile_length: float 
* tile_width: float 
* tile_height: float 
* rows: int 
* columns: int 
* margin: float
* uneven_depth: float
* seed: str
* segments: int
* peak_count: tuple[int,int]|int

``` python
import cadquery as cq
from cqterrain.material import uneven_blocks

blocks = uneven_blocks(
    tile_length = 10, 
    tile_width = 5, 
    tile_height= 5, 
    rows = 5, 
    columns = 6, 
    margin = 2,
    uneven_depth = 2.5,
    seed='test',
    segments = 10,
    peak_count = (14,15)
)

show_object(blocks)
```

![](image/material/02.png)


* [source](../src/cqterrain/material/uneven_blocks.py)
* [example](../example/material/uneven_blocks.py)
* [stl](../stl/material_uneven_blocks.stl)

----

## uneven_centered_blocks

List of uneven blocks centered at the 0,0 origin point.

### paramaters
* tile_length: float 
* tile_width: float 
* tile_height: float 
* rows: int 
* columns: int 
* margin: float
* uneven_depth: float
* seed: str
* segments: int
* peak_count: tuple[int,int]|int

``` python
import cadquery as cq
from cqterrain.material import uneven_centered_blocks

blocks = uneven_centered_blocks(
    tile_length = 10, 
    tile_width = 5, 
    tile_height= 5, 
    rows = 5, 
    columns = 6, 
    margin = 2,
    uneven_depth = 2.5,
    seed='test',
    segments = 10,
    peak_count = (14,15)
)

block_line = cq.Workplane("XY")

for i, b in enumerate(blocks):
    show_object(b.translate((0,i*6,0)))
```

![](image/material/03.png)


* [source](../src/cqterrain/material/uneven_centered_blocks.py)
* [example](../example/material/uneven_centered_blocks.py)
* [stl](../stl/material_centered_uneven_blocks.stl)


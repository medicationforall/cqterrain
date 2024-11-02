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
tile = cq.Workplane("XY").box(5,5,2).chamfer(0.8)
tile2 = cq.Workplane("XY").box(4,4,2).fillet(.5)
tile3 = cq.Workplane("XY").box(3,6,2).chamfer(0.5)
tiles = stone.make_stones(
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
```

![](image/stone/01.png)

* [source](../src/cqterrain/material/stone.py)
* [example](../example/material/stones.py)
* [stl](../stl/material_stones.stl)
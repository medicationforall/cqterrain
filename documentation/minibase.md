# Minibase

Collection is minibase shapes with magnet cutouts. 
The code for these is very simple most of these are just a loft operation.

![](image/minibase/06.png)

---

## Circle
### Parameters
* diameter: float
* height: float
* taper: float
* render_magnet: bool
* magnet_diameter: float
* magnet_height: float

``` python
result = circle(
    diameter = 25, 
    height = 3, 
    taper = -1,
    render_magnet = True, 
    magnet_diameter = 3, 
    magnet_height = 2
)
```

![](image/minibase/01.png)<br />

* [source](../src/cqterrain/minibase/circle.py)
* [example](../example/minibase/circle.py)
* [stl](../stl/minibase_circle.stl)

---

## Circle Uneven

### Parameters
* diameter: float
* base_height: float
* taper: float
* render_magnet: bool  
* magnet_diameter: float 
* magnet_height: float
* detail_height: float
* uneven_height: float
* peak_count: tuple[int,int]|int
* segments: int
* seed: str

``` python
import cadquery as cq
from cqterrain.minibase import circle_uneven

ex_base = circle_uneven(
    diameter = 45,
    base_height = 3,
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    detail_height = 3,
    uneven_height = 4,
    peak_count = (9,10),
    segments = 6,
    seed="red"
)

show_object(ex_base)
```

![](image/minibase/08.png)<br />

* [source](../src/cqterrain/minibase/circle_uneven.py)
* [example](../example/minibase/circle_uneven.py)
* [stl](../stl/minibase_circle_uneven.stl)

---

## Ellipse
### Parameters
* x_diameter: float
* y_diameter: float
* height: float
* taper: float
* render_magnet: bool
* magnet_diameter: float
* magnet_height: float

``` python
result = ellipse(
    x_diameter=52, 
    y_diameter=90, 
    height=3, 
    taper=-1,
    render_magnet = True,  
    magnet_diameter=3, 
    magnet_height=2
)
```

![](image/minibase/02.png)<br />

* [source](../src/cqterrain/minibase/ellipse.py)
* [example](../example/minibase/ellipse.py)
* [stl](../stl/minibase_ellipse.stl)

---

## Ellipse Uneven

### Parameters
* length: float
* width: float
* base_height: float
* taper: float
* render_magnet: bool  
* magnet_diameter: float 
* magnet_height: float
* detail_height: float
* uneven_height: float
* peak_count: tuple[int,int]|int
* segments: int
* seed: str

``` python
import cadquery as cq
from cqterrain.minibase import ellipse_uneven

ex_base = ellipse_uneven(
    length = 40,
    width = 40,
    base_height = 3,
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    detail_height = 3,
    uneven_height = 4,
    peak_count = (9,10),
    segments = 6,
    seed="red"
)

show_object(ex_base)
```

![](image/minibase/11.png)<br />

* [source](../src/cqterrain/minibase/ellipse_uneven.py)
* [example](../example/minibase/ellipse_uneven.py)
* [stl](../stl/minibase_ellipse_uneven.stl)

---

## Hexagon
### Parameters
* diameter: float
* height: float
* taper: float
* render_magnet: bool
* magnet_diameter: float
* magnet_height: float

``` python
result = hexagon(
    diameter = 25,
    height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2
)
```

![](image/minibase/05.png)<br />

* [source](../src/cqterrain/minibase/hexagon.py)
* [example](../example/minibase/hexagon.py)
* [stl](../stl/minibase_hexagon.stl)

---

## Hexagon Uneven

### Parameters
* diameter: float
* base_height: float
* taper: float
* render_magnet: bool  
* magnet_diameter: float 
* magnet_height: float
* detail_height: float
* uneven_height: float
* peak_count: tuple[int,int]|int
* segments: int
* seed: str

``` python
import cadquery as cq
from cqterrain.minibase import hexagon_uneven

ex_base = hexagon_uneven(
    diameter = 45,
    base_height = 3,
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    detail_height = 3,
    uneven_height = 4,
    peak_count = (9,10),
    segments = 6,
    seed="red"
)

show_object(ex_base)
```

![](image/minibase/09.png)<br />

* [source](../src/cqterrain/minibase/hexagon_uneven.py)
* [example](../example/minibase/hexagon_uneven.py)
* [stl](../stl/minibase_hexagon_uneven.stl)

---

## make_magnet_outline
Utility function for making the magnet cutouts for the bases.

### Parameters
* shape_height: float 
* magnet_diameter: float
* magnet_height: float


## Rectangle
### Parameters
* length: float
* width: float
* height: float
* taper: float
* render_magnet: bool
* magnet_diameter: float
* magnet_height: float

``` python
result = rectangle(
    length = 25, 
    width = 25, 
    height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2
)
```

![](image/minibase/03.png)<br />

* [source](../src/cqterrain/minibase/rectangle.py)
* [example](../example/minibase/rectangle.py)
* [stl](../stl/minibase_rectangle.stl)

---

## Rectangle Uneven

### Parameters
* length: float
* width: float
* base_height: float
* taper: float
* render_magnet: bool  
* magnet_diameter: float 
* magnet_height: float
* detail_height: float
* uneven_height: float
* peak_count: tuple[int,int]|int
* segments: int
* seed: str

``` python
import cadquery as cq
from cqterrain.minibase import rectangle_uneven

ex_base = rectangle_uneven(
    length = 40,
    width = 40,
    base_height = 3,
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    detail_height = 3,
    uneven_height = 4,
    peak_count = (9,10),
    segments = 6,
    seed="red"
)

show_object(ex_base)
```

![](image/minibase/10.png)<br />

* [source](../src/cqterrain/minibase/rectangle_uneven.py)
* [example](../example/minibase/rectangle_uneven.py)
* [stl](../stl/minibase_rectangle_uneven.stl)

---

## Slot
### Parameters
* length: float 
* width: float 
* height: float 
* taper: float 
* render_magnet: bool
* magnet_diameter: float 
* magnet_height: float

``` python
result = slot(
    length = 24, 
    width = 50, 
    height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2
)
```

![](image/minibase/04.png)<br />

* [source](../src/cqterrain/minibase/slot.py)
* [example](../example/minibase/slot.py)
* [stl](../stl/minibase_slot.stl)
  
---

## Slot Uneven

### Parameters
* length: float
* width: float
* base_height: float
* taper: float
* render_magnet: bool  
* magnet_diameter: float 
* magnet_height: float
* detail_height: float
* uneven_height: float
* peak_count: tuple[int,int]|int
* segments: int
* seed: str

``` python
import cadquery as cq
from cqterrain.minibase import slot_uneven

ex_base = slot_uneven(
    length = 75,
    width = 25,
    base_height = 3,
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    detail_height = 3,
    uneven_height = 4,
    peak_count = (9,10),
    segments = 6,
    seed="red"
)

show_object(ex_base)
```

![](image/minibase/07.png)<br />

* [source](../src/cqterrain/minibase/slot_uneven.py)
* [example](../example/minibase/slot_uneven.py)
* [stl](../stl/minibase_slot_uneven.stl)

---
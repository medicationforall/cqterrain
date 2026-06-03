# Swivel Documentation

## index
* [Swivel Base](#swivel-base)
* [Swivel Top](#swivel-top)

---

## Swivel Base 

### parameters
* diameter:float = 30
* height:float = 6
* chamfer:float = 1.5
* top_width:float = 2
* channel_width:float = 1
* magnet_diameter:float = 3.2
* magnet_height:float = 2.4
* cut_height:float|None = None
* render_greeble:bool = True
* greeble_count:int = 6

``` python
import cadquery as cq
from cqterrain.swivel import SwivelBase

bp = SwivelBase()

bp.diameter = 30
bp.height = 6
bp.chamfer = 1.5
bp.top_width = 2
bp.channel_width = 1

bp.magnet_diameter = 3.2
bp.magnet_height = 2.4
bp.cut_height = None

bp.render_greeble = True
bp.greeble_count = 6

bp.make()
ex_base = bp.build()

show_object(ex_base)
```

![](image/swivel/01.png)

* [source](../src/cqterrain/swivel/SwivelBase.py)
* [example](../example/swivel/swivel_base.py)
* [stl](../stl/swivel_base.stl)

---

## Swivel Top

### parameters
* diameter:float = 30
* height:float = 3
* magnet_diameter:float = 3.2
* magnet_height:float = 2.4

``` python 
import cadquery as cq
from cqterrain.swivel import SwivelTop

bp = SwivelTop()

bp.diameter = 30
bp.height = 3

bp.magnet_diameter = 3.2
bp.magnet_height = 2.4

bp.make()
ex_top = bp.build()

show_object(ex_top)
```

![](image/swivel/02.png)

* [source](../src/cqterrain/swivel/SwivelTop.py)
* [example](../example/swivel/swivel_top.py)
* [stl](../stl/swivel_top.stl)


# Crystal

---

## Crystal
Just a hardcoded implementation of an obelisk

``` python
import cadquery as cq
from cqterrain import obelisk

model = obelisk(
        base_width=20.0,
        base_height=0.5,
        inset_width=25.0,
        inset_height=3.1,
        mid_width=25.0,
        mid_height=2.0,
        top_width=35.0,
        top_height=40.0,
        height=70.0,
        faces=7,
        intersect=True
    ).rotate((0,0,1),(0,0,0),0)

show_object(model)
```

![](image/crystal/01.png)

* [source](../src/cqterrain/obelisk.py)
* [example](../example/crystal/crystal.py)
* [stl](../stl/crystal.stl)
  
---

## Crystal Random
Method for creating a psuedo random crystal like looking structure.

### parameters
* height: tuple[float,float,float]|float -min,max,step
* base_width: tuple[float,float,float]|float
* base_height: tuple[float,float,float]|float
* inset_width: tuple[float,float,float]|float
* inset_height: tuple[float,float,float]|float
* mid_height: tuple[float,float,float]|float
* mid_width: tuple[float,float,float]|float
* top_height: tuple[float,float,float]|float
* top_width: tuple[float,float,float]|float
* faces: tuple[int,int,int]|int - min,max,step
* seed: str|None
* intersect: bool

``` python
import cadquery as cq
from cqterrain.crystal import crystal_random

ex_crystal,ex_height = crystal_random(
    height = (50,80,2.5),#min,max,step
    base_width = 20.0,
    base_height = 0.5,
    inset_width = 25.0,
    inset_height = 3.1,
    mid_height = (2.0,10.0,0.5),
    mid_width = (20,35.0,2.5),
    top_height = (20,40,5),
    top_width = (20,35.0,2.5),
    faces=(5,10,2),#min,max,step
    seed='purple',
    intersect = True
)

# show_object(model)
```

![](image/crystal/02.png)

* [source](../src/cqterrain/crystal_random.py)
* [example](../example/crystal/crystal_random.py)
* [stl](../stl/crystal_random.stl)
  
---

## Crytal Random Group
Example of creating a group of crystals by specific seeds.

``` python
import cadquery as cq
from cqterrain.crystal import crystal_random

def crystal_adder():
    # closure
    count = 0
    def add_crystal(loc:cq.Location)->cq.Shape:
        nonlocal count
        count += 1
        adder_seed = f"blue_{count}"
        crystal,crystal_height = crystal_random(
            height = (50,75,2.5), 
            base_height = 0.5,
            inset_height = (5.0,10.0,1.0),
            mid_height = (1.0,10.0,1.0),
            mid_width = (20,25.0,2.5),
            top_height=(20,65,5),
            seed=adder_seed,
            faces=(4,10,1),
            intersect = True
        )
        
        crystal = crystal.translate((0,0,crystal_height/2)).union(cq.Workplane("XY").text(adder_seed,10,5).translate((0,25,30)))
        return crystal.val().located(loc) #type:ignore
    return add_crystal

size = 5
group = (
    cq.Workplane("XY")
    .rarray(
    xSpacing = 50, 
    ySpacing = 50,
    xCount = size, 
    yCount= size,
    center = True)
    .eachpoint(callback = crystal_adder())
)

show_object(model)
```

![](image/crystal/03.png)
![](image/crystal/04.png)

* [example](../example/crystal/crystal_random_group.py)
* [stl](../stl/crystal_random_group.stl)
  
---
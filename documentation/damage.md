# Damage

## Blast

### Parameters
* seed: str
* height: float
* count: tuple[int,int]
* x_jiggle: tuple[int,int] | int - can be tuple or int
* y_jiggle: tuple[int,int] | int - can be tuple or int
* ring_params: list[dict]

``` python
result = damage.blast(
    seed="test",
    height=10,
    count = (5,10),
    x_jiggle = (-2,2), 
    y_jiggle = 0,
    ring_params = [
        {"radius":(35,50), "start_angle":0}, 
        {"radius":25,"start_angle":30}
    ]
)
```

![](image/damage/07.png)<br />

if given a height of 0 will return the wire instead.

![](image/damage/08.png)<br />

* [source](../src/cqterrain/damage/blast.py)
* [example](../example/damage/blast.py)
* [stl 1](../stl/damage_blast_1.stl)
* [stl 2](../stl/damage_blast_2.stl)
* [stl 3](../stl/damage_blast_3.stl)

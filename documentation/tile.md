# Tile

## Basket Weave
### Parameters
* length - length of a single brick
* width - width of a single brick
* height
* padding - space between bricks

``` python
result = tile.basketweave(
    length = 4,
    width = 2,
    height = 1,
    padding = .5
)
```

![](image/tile/01.png)<br />

* [source](../src/cqterrain/tile/basketweave.py)
* [example](../example/tile/basketweave.py)
* [stl](../out/tile_basketweave.stl)

## Chamfer Frame
### Parameters
* length
* width
* height
* chamfer_length
* padding
* frame_width
* internal_height_cut

``` python
result = tile.chamfer_frame(
    length = 10,
    width = 10,
    height = 2,
    chamfer_length = 3,
    padding = .5,
    frame_width = 1.5,
    internal_height_cut = 1
)
```

![](image/tile/02.png)<br />

* [source](../src/cqterrain/tile/chamferframe.py)
* [example](../example/tile/chamfer_frame.py)
* [stl](../out/tile_chamfer_frame.stl)


## Octagon With Dots
### Parameters
* tile_size
* chamfer_size
* mid_tile_size
* spacing

``` python
result = tile.octagon_with_dots_2(
    tile_size = 5,
    chamfer_size = 1.2,
    mid_tile_size = 1.6,
    spacing = .5
)
```

![](image/tile/03.png)<br />

* [source](../src/cqterrain/tile/octagonWithDots.py)
* [example](../example/tile/octagon_with_dots.py)
* [stl](../out/tile_octagon_with_dots.stl)

#### Example
![](image/tile/04.png)<br />

## Plain
### Parameters
* length
* width
* height
* padding

``` python
result = tile.plain(
    length = 10,
    width = 10,
    height = 2,
    padding = 1
)
```

![](image/tile/05.png)<br />

* [source](../src/cqterrain/tile/plain.py)
* [example](../example/tile/plain.py)
* [stl](../out/tile_plain.stl)

## Rivet
### Parameters
* length
* width
* height
* padding
* internal_padding
* rivet_height
* rivet_radius

``` python
result = tile.rivet(
    length = 10,
    width = 10,
    height = 2,
    padding = 1,
    internal_padding = 2.5,
    rivet_height = 2.5,
    rivet_radius = .5
)
```

![](image/tile/06.png)<br />

* [source](../src/cqterrain/tile/rivet.py)
* [example](../example/tile/rivet.py)
* [stl](../out/tile_rivet.stl)

## Slot
### Parameters
* length
* width
* height
* padding
* slot_length_padding
* slot_width_offset
* slot_width
* slot_height

``` python
result = tile.slot(
    length = 10,
    width = 10,
    height = 2,
    padding = 1,
    slot_length_padding = 3,
    slot_width_offset = 1.5,
    slot_width = 1,
    slot_height = 0.5
)
```

![](image/tile/07.png)<br />

* [source](../src/cqterrain/tile/slot.py)
* [example](../example/tile/slot.py)
* [stl](../out/tile_slot.stl)

## Slot diagonal
### Parameters
* tile_size
* height
* slot_width
* slot_height
* slot_length_padding
* slot_width_padding
* slot_width_padding_modifier

``` python
result = tile.slot_diagonal(
    tile_size = 21,
    height = 2,
    slot_width = 2,
    slot_height = 2,
    slot_length_padding = 7,
    slot_width_padding = 2,
    slot_width_padding_modifier = .25
)
```

![](image/tile/08.png)<br />

* [source](../src/cqterrain/tile/slotDiagonal.py)
* [example](../example/tile/slot_diagonal.py)
* [stl](../out/tile_slot_diagonal.stl)

## Star
### Parameters
* length
* width
* height
* points
* outer_radius
* inner_radius
* padding

``` python
result = tile.star(
    length = 10,
    width = 10,
    height = 1,
    points = 4,
    outer_radius = 5,
    inner_radius = 3,
    padding = .5
)
```

![](image/tile/09.png)<br />

* [source](../src/cqterrain/tile/star.py)
* [example](../example/tile/star.py)
* [stl](../out/tile_star.stl)

## Windmill
### Parameters
* tile_size
* height
* padding

``` python
result = tile.windmill(
    tile_size = 10,
    height = 1,
    padding = 0.5
)
```

![](image/tile/10.png)<br />

* [source](../src/cqterrain/tile/windmill.py)
* [example](../example/tile/windmill.py)
* [stl](../out/tile_windmill.stl)

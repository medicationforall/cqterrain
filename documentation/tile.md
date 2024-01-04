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

## Bolt Panel
### Parameters
* length 
* width
* height 
* chamfer - appliet to the z face of the tile, can be 0 or None 
* radius_outer - outer radius of the bolt
* radius_internal - internal radius of the bolt
* cut_height - how deep the inset is of the bolt
* padding - distance of the bolts from the corners of the tile

``` python
result = tile.bolt_panel(
    length = 10, 
    width = 10, 
    height = 2, 
    chamfer = .5, 
    radius_outer=1,
    radius_internal=0.5,
    cut_height=0.5,
    padding = 2
)
```

![](image/tile/13.png)<br />

* [source](../src/cqterrain/tile/boltpanel.py)
* [example](../example/tile/boltPanel.py)
* [stl](../out/tile_bolt_panel.stl)


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

## Carton
### Parameters
* length
* width
* height
* line_width
* line_depth
* x_divisor
* y_divisor

``` python
result = tile.carton(
    length=60, 
    width=60, 
    height = 4,
    line_width = 3,
    line_depth = 1.5,
    x_divisor = 3,
    y_divisor = 2
)
```

![](image/tile/16.png)<br />

* [source](../src/cqterrain/tile/carton.py)
* [example](../example/tile/carton.py)
* [stl](../out/tile_carton.stl)

## Conduit
### Parameters
* length - length of the tile
* width - with of the tile
* height - height of the tile
* frame - size of the frame can be 0
* frame_depth - depth of the frame that the pipe is set into, can be zero
* pipe_count - hard coded pipe count. If falsy the pipes count will be determined by the witdth of the tile and the diameter of the pipe.
* radius - radius of the pipe
* inner_radius - internal radius of the inner pope
* segment_length - size of the pipe segments
* space - spece between the pipe segments
* pipe_padding - padding between pipes

``` python
result = tile.conduit(
    length = 25,
    width = 25,
    height = 4,
    frame= 1,
    frame_depth =3,
    pipe_count = None,
    radius = 4,
    inner_radius = 3,
    segment_length = 6,
    space = 4,
    pipe_padding = 1
)
```

![](image/tile/15.png)<br />

* [source](../src/cqterrain/tile/conduit.py)
* [example](../example/tile/conduit.py)
* [stl](../out/tile_conduit.stl)


## Glyph
### Parameters
* length
* width
* height
* padding

``` python
result = tile.glyph(
    length = 4,
    width = 2,
    height = 1,
    padding = .5
)
```

![](image/tile/14.png)<br />

* [source](../src/cqterrain/tile/glyph.py)
* [example](../example/tile/glyph.py)
* [stl](../out/tile_glyph.stl)


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

## Rivet Round
### Parameters
* radius 
* height
* rivet_height
* rivet_radius
* padding
* rivet_count

``` python
result = tile.rivet_round(
    radius = 10, 
    height = 2,
    rivet_height = 0.5,
    rivet_radius = .5,
    padding = 1,
    rivet_count = 5
)
```

![](image/tile/11.png)<br />

* [source](../src/cqterrain/tile/rivetRound.py)
* [example](../example/tile/rivetRound.py)
* [stl](../out/tile_rivet_round.stl)

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


## Spoked Wheel
### Parameters
* radius
* height
* frame
* inner_radius
* spoke_width
* spoke_height
* spoke_fillet
* spoke_count
* frame_chamfer
* inner_chamfer

``` python
result = tile.spoked_wheel(
    radius = 10,
    height = 2,
    frame = 2,
    inner_radius = 3,
    spoke_width = 2,
    spoke_height = 1.5,
    spoke_fillet = .5,
    spoke_count = 12,
    frame_chamfer = .5,
    inner_chamfer = .5
)
```

![](image/tile/12.png)<br />

* [source](../src/cqterrain/tile/spokedWheel.py)
* [example](../example/tile/spokedWheel.py)
* [stl](../out/tile_spoked_wheel.stl)

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

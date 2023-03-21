# Tile

## Basket Weave
### Parameters
* length
* width
* height
* padding

``` python
tile = tile.basketweave(
    length = 4,
    width = 2,
    height = 1,
    padding = .5
)
```

## Chamfer Plain
### Parameters
* length
* width
* height
* chamfer_length
* padding
* frame_width
* internal_height_cut

``` python
tile = tile.chamfer_frame(
    length = 10,
    width = 10,
    height = 2,
    chamfer_length = 3,
    padding = .5,
    frame_width = 1.5,
    internal_height_cut = 1
)
```

## Octagon With Dots
### Parameters
* tile_size
* chamfer_size
* mid_tile_size
* spacing

``` python
tile = tile.octagon_with_dots_2(
    tile_size = 5,
    chamfer_size = 1.2,
    mid_tile_size = 1.6,
    spacing = .5
)
```

## Plain
### Parameters
* length
* width
* height
* padding

``` python
tile = tile.plain(
    length = 10,
    width = 10,
    height = 2,
    padding = 1
)
```

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
tile = tile.rivet(
    length = 10,
    width = 10,
    height = 2,
    padding = 1,
    internal_padding = 2.5,
    rivet_height = 2.5,
    rivet_radius = .5
)
```

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
tile = tile.slot(
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

## Star
### Parameters
* length
* points
* inner_radius
* padding

``` python
tile = tile.star(
    length = 8.5,
    points = 9,
    inner_radius = 2,
    padding = 1
)
```

## Windmill
### Parameters
* tile_size
* height
* padding

``` python
tile = tile.windmill(
    tile_size = 10,
    height = 1,
    padding = 0.5
)
```

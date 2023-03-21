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

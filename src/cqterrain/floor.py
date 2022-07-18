import cadquery as cq
from cadqueryhelper import parts
from cadqueryhelper import grid

def make_floor(dim=[100, 100, 3]):
    return parts.make_cube(dim[0], dim[1], dim[2])

def make_tile_floor(tile, dim=[100, 100, 3]):
    print('make_tile_floor')

    tile_grid = grid.make_grid(part=tile, dim = [6,6])
    floor = make_floor(dim)

    tile_grid.add(floor)

    comp = tile_grid.toCompound()
    return comp

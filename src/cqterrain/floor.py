import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import grid
import math

def make_floor(dim=[100, 100, 3]):
    return shape.cube(dim[0], dim[1], dim[2])

def make_tile_floor(tile, dim=[100, 100, 3]):
    tile_width = 5
    tile_length = 5
    tile_height = 5
    floor_width = dim[0]
    floor_length = dim[1]
    floor_height = dim[2]

    tile_meta = __resolve_tile_meta(tile)

    if tile_meta and 'width' in tile_meta and 'length' in tile_meta:
        tile_width = tile_meta['width']
        tile_length = tile_meta['length']
        tile_height = tile_meta['height']
    else:
        raise Exception('Could not resolve width and or length from tile metadata', tile_meta)

    columns = math.floor(floor_width/tile_width)
    rows = math.floor(floor_length/tile_length)

    tile_grid = grid.make_grid(part=tile, dim = [tile_width, tile_length], columns = columns, rows = rows)
    floor = make_floor(dim)
    #comp_tile_grid = tile_grid.toCompound()

    floor_assembly = cq.Assembly()
    floor_assembly.add(tile_grid, name="tiles", loc=cq.Location(cq.Vector(0, 0, (tile_height/2) + (floor_height/2))))
    floor_assembly.add(floor, name="floor")
    comp_floor = floor_assembly.toCompound()

    meta = {'type':'floor', 'height':tile_height +dim[2] , 'length':floor_length, 'width':floor_width}
    comp_floor.metadata = meta

    return comp_floor

def __resolve_tile_meta(tile):
    meta = None
    tile_attributes = dir(tile)
    if 'metadata' in tile_attributes:
        meta = tile.metadata
    return meta

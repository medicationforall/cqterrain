import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import grid
import math

def make_wall(length = 100, width = 3, height = 50):
    return shape.cube(length, width, height)

def make_tile_wall(inside_tile=None, oustide_tile=None, length = 100, width = 3, height = 50):
    wall_part = make_wall(length = length, width = width, height = height)

    wall_assembly = cq.Assembly()
    wall_assembly.add(wall_part, name="wall")

    if inside_tile:
        print('found inside tile')
        inside_meta = __resolve_tile_meta(tile)
        inside_width = inside_meta['width']
        inside_length = inside_meta['length']
        inside_height = inside_meta['height']
        inside_columns = math.floor(width/inside_width)
        inside_rows = math.floor(length/inside_length)
        inside_grid = grid.make_grid(part=inside_tile, dim = [inside_width, inside_length], columns = columns, rows = rows)
        wall_assembly.add(inside_grid, name="insideGrid")

    comp_wall = wall_assembly.toCompound()

    meta = {'type':'wall', 'height':height, 'length':length, 'width':width}
    comp_wall.metadata = meta

    return comp_wall

def __resolve_tile_meta(tile):
    meta = None
    tile_attributes = dir(tile)
    if 'metadata' in tile_attributes:
        meta = tile.metadata
    return meta

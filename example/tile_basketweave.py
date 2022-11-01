import cadquery as cq
from cqterrain import tile

tile = tile.basketweave(length = 4, width = 2, height = 1, padding = .5)
scene = cq.Workplane("XY").add(tile)

cq.exporters.export(scene,'out/tile_basketweave.stl')

import cadquery as cq
from cqterrain import tile

tile = tile.star(length=8.5, points=9, inner_radius=2, padding = 1)
scene = cq.Workplane("XY").add(tile)

cq.exporters.export(scene,'out/tile_star.stl')
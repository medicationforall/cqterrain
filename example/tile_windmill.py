import cadquery as cq
from cqterrain import tile

tile = tile.windmill(tile_size=10, height=1, padding=0.5, )
scene = cq.Workplane("XY").add(tile)

cq.exporters.export(scene,'out/tile_windmill.stl')

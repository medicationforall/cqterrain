import cadquery as cq
from cqterrain import tile

result = tile.bolt_panel(
    length = 5, 
    width = 6, 
    height = 2, 
    chamfer = .5, 
    radius_outer = .4,
    radius_internal = 0.2,
    cut_height = 0.25,
    padding = 1
)

cq.exporters.export(result,'out/tile_bolt_panel.stl')
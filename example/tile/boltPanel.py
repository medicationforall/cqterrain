import cadquery as cq
from cqterrain import tile

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

cq.exporters.export(result,'out/tile_bolt_panel.stl')
import cadquery as cq
from cqterrain import tile

result = tile.apricorn(
    length = 30, 
    width = 25, 
    height = 4,
    line_width = 2,
    line_depth = .5,
    center_radius = None,
    width_radius_divisor = 4
)
#show_object(result)
cq.exporters.export(result,'stl/tile_apricorn.stl')
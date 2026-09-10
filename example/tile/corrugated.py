import cadquery as cq
from cqterrain.tile import corrugated

result = corrugated(
    length = 25,
    width = 25,
    height = 3,
    segment_length = 4,
    inner_width = 0.5
)

#show_object(result)
cq.exporters.export(result,'stl/tile_corrugated.stl')
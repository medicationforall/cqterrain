import cadquery as cq
from cqterrain.tile import truchet_circle_two

example_tile = truchet_circle_two(
    length=10,
    width=10,
    radius=2 
)

#show_object(example_tile)

cq.exporters.export(example_tile, "stl/tile_truchect_circle_two.stl")
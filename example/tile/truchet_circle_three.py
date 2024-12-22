import cadquery as cq
from cqterrain.tile import truchet_circle_three

example_tile = truchet_circle_three(
    length=10,
    width=10,
    radius=2 
)

#show_object(example_tile)

cq.exporters.export(example_tile, "stl/tile_truchect_circle_three.stl")
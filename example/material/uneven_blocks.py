import cadquery as cq
from cqterrain.material import uneven_blocks

blocks = uneven_blocks(
    tile_length = 10, 
    tile_width = 5, 
    tile_height= 5, 
    rows = 5, 
    columns = 6, 
    margin = 2,
    uneven_depth = 2.5,
    seed='test',
    segments = 10,
    peak_count = (14,15)
)

#show_object(blocks)

cq.exporters.export(blocks,'stl/material_uneven_blocks.stl')
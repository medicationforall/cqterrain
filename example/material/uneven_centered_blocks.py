import cadquery as cq
from cqterrain.material import uneven_centered_blocks

blocks = uneven_centered_blocks(
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

block_line = cq.Workplane("XY")

for i, b in enumerate(blocks):
    #show_object(b.translate((0,i*6,0)))
    block_line = block_line.union(b.translate((0,i*6,0)))
    
cq.exporters.export(block_line,'stl/material_centered_uneven_blocks.stl')
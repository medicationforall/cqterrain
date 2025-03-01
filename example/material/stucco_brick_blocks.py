import cadquery as cq
from cqterrain.material import stacked_wave_form_map, stucco_brick_blocks

map = stacked_wave_form_map(
    size = (10,15),
    seed = 'test',
    cell_types = ['block','block','empty','block']
)

ex_matarial = stucco_brick_blocks(
    map,
    length = 10, 
    width = 5, 
    height = 5,
    spacing = 2
)

#show_object(ex_matarial)
cq.exporters.export(ex_matarial, 'material_stucco_brick_blocks.stl')
import cadquery as cq
from cqterrain.door import pull_handle

handle_ex = pull_handle(
    length = 3, 
    width = 4, 
    height = 6,
    handle_length = 1,
    handle_width_padding = 1,
    handle_z_margin = 2,
    handle_base_chamfer = 1,
    mirrored = False
)
#show_object(handle_ex)#.translate((-25,0,0)))
cq.exporters.export(handle_ex,'stl/door_pull_handle.stl')

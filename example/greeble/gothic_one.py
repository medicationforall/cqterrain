import cadquery as cq
from cqterrain.greeble import gothic_one

result = gothic_one(
    length = 15,
    width = 4,
    height = 20,
    frame_size = .5,
    pane_width = 1,
    inside_frame_width = -.5,
    inside_frame_size = .5,
    diamond_frame_size = 1,
    diamond_frame_width = -.25,
    diamond_inside = -.5
)

#show_object(tile_ex.translate((0,30,0)))
cq.exporters.export(result,'stl/greeble_gothic_one.stl')
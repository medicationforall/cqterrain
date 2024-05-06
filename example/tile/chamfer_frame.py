import cadquery as cq
from cqterrain import tile

result = tile.chamfer_frame(
    length = 10,
    width = 10,
    height = 2,
    chamfer_length = 3,
    padding = .5,
    frame_width = 1.5,
    internal_height_cut = 1
)

cq.exporters.export(result,'stl/tile_chamfer_frame.stl')

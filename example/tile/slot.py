import cadquery as cq
from cqterrain import tile

result = tile.slot(
    length = 10,
    width = 10,
    height = 2,
    padding = 1,
    slot_length_padding = 3,
    slot_width_offset = 1.5,
    slot_width = 1,
    slot_height = 0.5
)

cq.exporters.export(result,'stl/tile_slot.stl')

import cadquery as cq
from cqterrain import tile

result = tile.slot_diagonal(
    tile_size = 21,
    height = 2,
    slot_width = 2,
    slot_height = 2,
    slot_length_padding = 7,
    slot_width_padding = 2,
    slot_width_padding_modifier = .25
)

cq.exporters.export(result,'stl/tile_slot_diagonal.stl')

import cadquery as cq
import math

def slot_diagonal(
    tile_size = 21,
    height = 2,
    slot_width = 2,
    slot_height = 2,
    slot_length_padding = 7,
    slot_width_padding = 2,
    slot_width_padding_modifier = .25
):
    size = math.floor(tile_size / (slot_width + slot_width_padding))
    tile = cq.Workplane("XY").box(tile_size, tile_size, height)
    slots = (cq.Workplane("XY"))

    slot = cq.Workplane("XY").slot2D(tile_size,slot_width).extrude(slot_height)
    slots = slots.union(slot)

    for i in range(1,math.ceil((size+1)/2)):
        slot = (
            cq.Workplane("XY")
            .slot2D(tile_size - (slot_length_padding*i),slot_width)
            .extrude(slot_height)
        )
        y_translate = i*(slot_width+slot_width_padding+(slot_width_padding_modifier*1))
        slots = slots.union(slot.translate((0,y_translate,0)))

    for i in range(1,math.ceil((size+1)/2)):
        slot = (
            cq.Workplane("XY")
            .slot2D(tile_size - (slot_length_padding*i),slot_width)
            .extrude(slot_height)
        )
        y_translate = i*(slot_width+slot_width_padding+(slot_width_padding_modifier*1))
        slots = slots.union(slot.translate((0,-1*y_translate,0)))

    slots = (
        slots
        .rotate((0,0,1),(0,0,0),45)
    )

    tile = tile.cut(slots)
    return tile
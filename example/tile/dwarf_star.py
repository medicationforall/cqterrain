import cadquery as cq
from cqterrain.tile import dwarf_star

result = dwarf_star(
        length = 15,
        width = 15,
        height = 2,
        depth = .6, 
        margin = .6,
        inner_band_width = 1,
        inner_track_width = 1
)
#show_object(result)

cq.exporters.export(result,'stl/tile_dwarf_star.stl')
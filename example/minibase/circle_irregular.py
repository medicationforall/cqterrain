import cadquery as cq
from cqterrain.minibase import circle_irregular

def custom_item(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
    )

ex_base = circle_irregular(
    diameter = 40, 
    base_height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    min_height = 1,
    max_height = 3.5,
    overlap = 20,
    col_size = 5,
    row_size = 8,
    max_columns = 2,
    max_rows = 2,
    passes_count = 3000,
    seed = "seed",
    tile_styles = [custom_item],
    debug = False
)

#show_object(ex_base)
cq.exporters.export(ex_base,'stl/minibase_circle_irregular.stl')
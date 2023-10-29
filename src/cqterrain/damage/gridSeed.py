import cadquery as cq

def grid_seed(
        shape_callback=None, 
        count=16, 
        seed_base="blast", 
        columns=8, 
        length = 50, 
        width = 50, 
        z_transform = 2.5
    ):
    shape_grid = cq.Workplane("XY")
    row_count = -1
    for i in range(count):
        string_seed = f"{seed_base}{i}"
        gen_shape, text = shape_callback(string_seed)
        
        col_count = i % columns
        if col_count == 0:
            row_count += 1
    
        shape_grid.add(gen_shape.translate((
            length*col_count,
            -width*row_count,
            0
        )))
        
        shape_grid.add(text.translate((
            length*col_count,
            -width*row_count,
            z_transform
        )))
    return shape_grid
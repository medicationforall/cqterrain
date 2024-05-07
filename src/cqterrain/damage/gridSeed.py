import cadquery as cq
from typing import Callable

def grid_seed(
        shape_callback:Callable[[str], tuple[cq.Workplane, cq.Workplane]]|None=None, 
        count:int = 16, 
        seed_base:str = "blast", 
        columns:int = 8, 
        length:float = 50, 
        width:float = 50, 
        z_transform:float = 2.5
    ) -> cq.Workplane:
    '''
    Helper for previewing randomly generated blast patterns.
    '''
    shape_grid = cq.Workplane("XY")
    row_count = -1
    for i in range(count):
        string_seed = f"{seed_base}{i}"

        if not shape_callback:
            raise Exception('Please supply callback')
        
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
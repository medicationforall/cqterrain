# Copyright 2023 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
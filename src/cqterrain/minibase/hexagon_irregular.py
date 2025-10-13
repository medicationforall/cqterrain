# Copyright 2025 James Adams
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
from . import hexagon, base_irregular

def custom_item(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
    )

def hexagon_irregular(
    diameter:float = 40,
    base_height:float = 3, 
    taper:float = -1,
    render_magnet:bool = True,  
    magnet_diameter:float = 3, 
    magnet_height:float = 2,
    min_height:float = 1,
    max_height:float = 3.5,
    overlap:float = 20,
    col_size:float = 5,
    row_size:float = 8,
    max_columns:int = 2,
    max_rows:int = 2,
    passes_count:int = 3000,
    seed:str = "seed",
    tile_styles:list = [custom_item],
    debug:bool = False
):
    base:cq.Workplane = hexagon(
        diameter = diameter, 
        height = base_height, 
        taper = taper,
        render_magnet = render_magnet,  
        magnet_diameter = magnet_diameter, 
        magnet_height = magnet_height
    )

    return base_irregular(
        base,
        min_height = min_height,
        max_height = max_height,
        overlap = overlap,
        col_size = col_size,
        row_size = row_size,
        max_columns = max_columns,
        max_rows = max_rows,
        passes_count = passes_count,
        seed = seed,
        tile_styles = tile_styles,
        debug = debug
    )
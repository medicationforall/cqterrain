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
import random
from numpy import arange
from . import book

def resolve_range_val(v)->float|int:
    if type(v) == tuple:
        range_values = arange(v[0],v[1]+v[2],v[2])
        v = random.choice(range_values)
    return v

def book_random(
    length:tuple[float,float,float]|float = 3, 
    width:tuple[float,float,float]|float = 10, 
    height:tuple[float,float,float]|float = 12,
    binder_width:tuple[float,float,float]|float = 0.5,
    page_width_inset:float = 1,
    page_height_inset:float = 1,
    bottom_align:bool = False,
    fillet:float = 0.5,
    seed:str|None = "test"
):
    if seed:
        random.seed(seed)

    #print(f'random_book {seed} {length=} {width=} {height=}')
        
    length = resolve_range_val(length)
    width = resolve_range_val(width)
    height = resolve_range_val(height)
    binder_width = resolve_range_val(binder_width)
    page_width = width - page_width_inset
    page_height = height - page_height_inset
    fillet = resolve_range_val(fillet)
    #rint(f'random_book {seed} {length=} {width=} {height=}')
    
    return book(
        length= length, 
        width = width, 
        height = height,
        binder_width = binder_width,
        page_width = page_width,
        page_height = page_height,
        bottom_align = bottom_align,
        fillet = fillet
    ),(length,width,height)
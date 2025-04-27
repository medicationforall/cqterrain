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
from . import book_random


def resolve_range_val(v)->int:
    if type(v) == tuple:
        range_values = arange(v[0],v[1]+v[2],v[2])
        v = random.choice(range_values)
    return v

def book_generator(
        seed:str = "test",
        length:tuple[float,float,float]|float = (2.0,4.0,0.5),
        width:tuple[float,float,float]|float = (8,11,0.5), 
        height:tuple[float,float,float]|float = (8,12,0.5),
        binder_width:tuple[float,float,float]|float = .5,
        page_width_inset:float = 1,
        page_height_inset:float = 1,
        bottom_align:bool = True
    ):
    count = 0
    
    def add_book(loc:cq.Location)->cq.Shape:
        nonlocal count
        count+=1
        add_seed = f'{seed}_{count}'
        #log(f'{add_seed}')
        gen_book,dim = book_random(
            length = length,
            width = width, 
            height = height,
            binder_width = binder_width,
            page_width_inset = page_width_inset,
            page_height_inset = page_height_inset,
            bottom_align = bottom_align,
            seed=add_seed
        )
        gen_book = (
            gen_book
            .rotate((0,1,0),(0,0,0),90)
            .rotate((0,0,1),(0,0,0),90)
        ).translate((-dim[1]/2,dim[2]/2,dim[0]/2))
        # I think I need to translate by the books length
        return gen_book.val().located(loc)#type:ignore
    return add_book

def books(
        count:tuple[int,int,int]|int = 10,
        length:tuple[float,float,float]|float = (2.0,4.0,0.5),
        width:tuple[float,float,float]|float = (8,11,0.5), 
        height:tuple[float,float,float]|float = (8,12,0.5),
        binder_width:tuple[float,float,float]|float = .5,
        page_width_inset:float = 1,
        page_height_inset:float = 1,
        bottom_align:bool = True,
        seed:str = "test"
    ):
    if seed:
        random.seed(seed)
    book_count:int = resolve_range_val(count)

    ex_book,dim_1 = book_random(
        length=length,
        width = width, 
        height = height,
        binder_width=binder_width,
        page_width_inset = page_width_inset,
        page_height_inset=page_height_inset,
        bottom_align = bottom_align,
        seed=None
    )
    ex_book = ex_book.translate((dim_1[0]/2,-dim_1[1]/2,dim_1[2]/2))

    adder_method = book_generator(
        length=length,
        width = width, 
        height = height,
        binder_width=binder_width,
        page_width_inset = page_width_inset,
        page_height_inset=page_height_inset,
        bottom_align = bottom_align,
        seed=seed
    )
    attach = ex_book

    if book_count > 2:
        for i in range(book_count-1):#type:ignore
            generated_book = (
                attach
                .faces(">X")
                .workplane()
                .eachpoint(adder_method))
            attach = attach.union(generated_book)

    x = attach.val().BoundingBox().xlen #type:ignore
    y = attach.val().BoundingBox().ylen #type:ignore
    z = attach.val().BoundingBox().zlen #type:ignore

    return attach,(x,y,z)


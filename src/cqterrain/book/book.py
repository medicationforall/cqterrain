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

def book(
    length:float = 3, 
    width:float = 10, 
    height:float = 12,
    binder_width:float = 0.5,
    page_width:float = 8,
    page_height:float = 11,
    bottom_align:bool = False,
    fillet:float = 0.5
):
    cover = cq.Workplane("XY").box(length, width, height)
    interior = cq.Workplane("XY").box(length-binder_width*2,width-binder_width,height)
    
    if not bottom_align:
        pages = cq.Workplane("XY").box(length-binder_width*2,page_width, page_height)
    else:
        height_diff = height - page_height
        pages = cq.Workplane("XY").box(length-binder_width*2,page_width, height-height_diff/2)
        pages = pages.translate((-0,0,-height_diff/4))

    page_offset = (width - page_width)/2
    #log(f'{page_offset=}')    
    if fillet:
        cover = cover.faces("-Y").edges("Z").fillet(fillet)
        
    b = (
        cq.Workplane("XY")
        .union(cover)
        .cut(interior.translate((0,binder_width/2,0)))
        .union(pages.translate((0,-page_offset+binder_width,0)))
    )
    
    return b
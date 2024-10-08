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

def bolt_panel(
        length:float = 10, 
        width:float = 10, 
        height:float = 2, 
        chamfer:float = .5, 
        radius_outer:float = 1,
        radius_internal:float = 0.5,
        cut_height:float = 0.5,
        padding:float = 2
    ) -> cq.Workplane:
    outline = (
        cq.Workplane("XY")
        .box(length, width, height)
    )
    
    if chamfer:
        outline = outline.faces("Z").chamfer(chamfer)
    
    cyl = (
        cq.Workplane("XY")
        .cylinder(height, radius_outer)
    )
    cyl_1 = (
        cq.Workplane("XY")
        .cylinder(height, radius_internal)
    )
    
    cyl_2 = (
        cq.Workplane("XY")
        .cylinder(height-cut_height, radius_outer)
    )
    
    cyl_i = (
        cq.Workplane("XY")
        .union(cyl_1)
        .add(cyl_2.translate((0,0,-cut_height/2)))
    )
    
    x_tran = length/2-padding
    y_tran = width /2-padding
    
    cut_cylinders = (
        cq.Workplane("XY")
        .add(cyl.translate((x_tran,y_tran,0)))
        .add(cyl.translate((-x_tran,y_tran,0)))
        
        .add(cyl.translate((x_tran,-y_tran,0)))
        .add(cyl.translate((-x_tran,-y_tran,0)))
    )
    
    cylinders = (
        cq.Workplane("XY")
        .add(cyl_i.translate((x_tran,y_tran,0)))
        .add(cyl_i.translate((-x_tran,y_tran,0)))
        
        .add(cyl_i.translate((x_tran,-y_tran,0)))
        .add(cyl_i.translate((-x_tran,-y_tran,0)))
    )
    
    result = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_cylinders)
        .union(cylinders)

    )
    return result
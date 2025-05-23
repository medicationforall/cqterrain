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

def hatch(
        connector:cq.Workplane, 
        radius:float = 11.5,
        height:float = 4,
        bolt_number:int = 8, 
        bolt_radius:float = 2, 
        bolt_height:float = 1,
        bolt_padding:float = -2,
        center_radius:float = 8,
        center_height:float = 1,
        center_cut_height:float = 2
    ) -> cq.Workplane:
    bolt = (
        cq.Workplane("XY")
        .polygon(6, bolt_radius)
        .extrude(bolt_height)
        .translate((bolt_padding,0,0))
    )
    
    def add_bolt(loc:cq.Location)->cq.Shape:
        return bolt.val().located(loc)#type:ignore
    
    bolt_arc =(
        cq.Workplane("XY")
        .polarArray(
            radius  = radius, 
            startAngle  = 0, 
            angle  = 360, 
            count  = bolt_number,
            fill = True,
            rotate = True
        )
        .eachpoint(add_bolt)
    )
    
    center_cut = cq.Workplane("XY").cylinder(center_cut_height, center_radius)
    fillet_val = height
    if fillet_val > center_radius:
        fillet_val = center_radius/2
        
    center = (
        cq.Workplane("XY")
        .cylinder(height, center_radius-1)
        .faces("Z").fillet(fillet_val-.01)
    )
    
    return (
        cq.Workplane("XY")
        .union(connector.rotate((0,1,0),(0,0,0),90))
        .union(bolt_arc.translate((0,0,height/2)))
        .cut(center_cut.translate((0,0,(center_cut_height/2)+bolt_height)))
        .union(center.translate((0,0,center_height)))
    )
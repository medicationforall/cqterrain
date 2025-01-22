# Copyright 2024 James Adams
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
import math

def ramp( 
    height:float = 71,
    inner_diameter:float = 76,
    diameter:float = 75+45,
    stair_height:float|None = 5.461538461538462,
    stair_count:int|None = None,
    distance_overlap:float = 1,
    debug:bool = False
) -> cq.Workplane:
    cut_cylinder = cq.Workplane("XY").cylinder(height, inner_diameter/2)
    outline = cq.Workplane("XY").cylinder(height, diameter/2)
    intersect = cq.Workplane("XY").box(diameter,diameter,height)
    
    if stair_count is None and stair_height is not None:
        stair_count = math.floor(height / stair_height)
    elif stair_count is not None:
        stair_height = height / stair_count
    else:
        raise Exception('stair_count and stair_height are None')
    
    stair_deg = 90 / stair_count
    
    #outline
    stair_outline = cq.Workplane("XY").cylinder(stair_height, diameter/2)
    stair_single = (
        cq.Workplane("XY")
        .union(stair_outline)
        .cut(cut_cylinder)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    )
    
    # make the last step
    
    stair_rough = (
        cq.Workplane("XY")
        .union(outline)
        .cut(cut_cylinder)
        .intersect(intersect.translate((diameter/2,diameter/2,0)))
    )
    
    last_step = (
        stair_single
        .rotate((0,0,1),(0,0,0),-stair_deg*(stair_count-1))
        .intersect(stair_rough)
    ).rotate((0,0,1),(0,0,0),stair_deg*(stair_count-1))
    
    outside_edge = last_step.faces("Z").edges(">X")
    inside_edge = last_step.faces("Z").edges("<X")

    #apply magic numbers for reasons
    distance_inside = inside_edge.vals()[0].Length()-0.01 #type:ignore
    distance = outside_edge.vals()[0].Length()+0.0675 #type:ignore
    
    pts = [(0,0),(distance_inside,stair_height),(0,stair_height)]
    pts_outside = [(0,0),(distance,stair_height),(0,stair_height)]
    distance_cut = (
        cq.Workplane("YZ")
        .polyline(pts)
        .close()
        .wire()
        .workplane(offset=(diameter/2 -inner_diameter/2)+distance_overlap)
        .polyline(pts_outside)
        .close()
        .wire()
        .loft(combine=True)
    ).translate((inner_diameter/2-distance_overlap/2,0,-stair_height/2))
    
    distance_cut_cap = (
        cq.Workplane("YZ")
        .polyline(pts)
        .close()
        .extrude(distance_overlap)
    )
    
    distance_cut = distance_cut.union(distance_cut_cap.translate(((inner_diameter/2-distance_overlap/2)-distance_overlap,0,-stair_height/2)))
    #return distance_cut

    #return stair_single.add(distance_cut).add(last_step)
    stair_single = stair_single.cut(distance_cut)
    #return stair_single

    stairs = cq.Workplane("XY")
    
    for i in range(stair_count):
        #log(f"add stair {i}, {stair_deg*i}")
        stairs = (
            stairs
            .translate((0,0,-stair_height*1))
            #.add(last_step.rotate((0,0,1),(0,0,0),-stair_deg*i))
            .union(stair_single.rotate((0,0,1),(0,0,0),-stair_deg*i))
        )
    
    if debug:
        return stairs.translate((0,0,height/2-stair_height/2)).add(stair_rough)
    else:
        return stairs.translate((0,0,height/2-stair_height/2)).intersect(stair_rough)
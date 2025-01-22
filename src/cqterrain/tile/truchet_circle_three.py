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

def truchet_circle_three(
        length:float = 10,
        width:float = 10,
        radius:float = 1.5
    ) -> cq.Workplane:
    torus_radius = length if length>width else width
    torus_radius = (torus_radius/2)
    
    cylinder = cq.Workplane("XY").cylinder(radius*2, width/2+radius/2)
    in_cylinder = cq.Workplane("XY").cylinder(radius*2, width/2-radius/2)
    torus = cylinder.cut(in_cylinder)
    outline = cq.Workplane('XY').box(length,width,radius*2)
    
    scene = (
        cq.Workplane("XY")
        .add(torus.translate((width/2,width/2,0)))
        .intersect(outline)
        .translate((0,0,0))
    )
    
    scene = scene.union(scene.rotate((0,0,1),(0,0,0),180))
    return scene
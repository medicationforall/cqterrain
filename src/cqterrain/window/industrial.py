# Copyright 2022 James Adams
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

def industrial(
        length:float = 20, 
        width:float = 4, 
        height:float = 40, 
        frame_width:float = 4, 
        sphere_radius:float = 1, 
        sphere_top:float = 2, 
        strut_chamfer:float = .7
    ) -> cq.Workplane:
    frame = cq.Workplane("XY").box(length, width, height)
    window = cq.Workplane("XY").box(length-(frame_width*2), width, height)
    combined = frame.cut(window)

    top_spheres = combined.edges("X").translate((0,0,-sphere_top)).sphere(sphere_radius, combine=False)
    bottom_spheres = combined.edges("X").translate((0,0,sphere_top)).sphere(sphere_radius, combine=False)

    combined = combined.edges("X").chamfer(strut_chamfer).cut(top_spheres).cut(bottom_spheres)
    return combined
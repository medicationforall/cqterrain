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
from . import pipe_face

def end():
    power_face = pipe_face(face_rotate=0)
    path = (
        cq.Workplane("ZY")
        .ellipseArc(
            x_radius = 11.51,
            y_radius = 11.51,
            angle1 = 90,
            angle2 = 180
            #rotation_angle=-30
        )
    )
    
    curve_shape = (
        power_face
        #.toPending()
        .sweep(path)
        #.rotate((0,1,0),(0,0,0),90)
        #.translate((x_radius/2,-1*(y_radius/2),0))
    )
    
    cut_cube = cq.Workplane("XY").box(21,24,4).translate((0,0,2))
    connector = (cq.Workplane("XY").cylinder(2, 11.5))
    
    curve_shape = (
        curve_shape
        .cut(cut_cube)
        .union(connector.translate((0,.5,-1)))
        .union(connector
             .rotate((1,0,0),(0,0,0),90)
             .translate((0,-10.51,-12))
        )
    ).rotate((0,0,1),(0,0,0),-90).rotate((1,0,0),(0,0,0),180)
    
    
    pip_height = 2.4 
    pip_radius = 1.56
    pip = (
        cq.Workplane("XY")
        .cylinder(pip_height,pip_radius)
        .rotate((0,1,0),(0,0,0),0)
    )
    
    y_translate = 10/2 +1.4
    magnet_cuts = (
        cq.Workplane("XY")
        .union(pip.translate((
            0,
            y_translate,
            0
        )))
        .union(pip.translate((
            0,
            -y_translate,
            0
        )))
    )
    
    curve_shape = (
        curve_shape
        .cut(magnet_cuts.translate((3.95,0,pip_height/2)))
        .cut(magnet_cuts.rotate((0,1,0),(0,0,0),90).translate((10.31,0,7.6)))
    )
    return curve_shape

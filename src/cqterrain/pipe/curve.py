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

def __add_connector_with_count(
        max_count:int=3
    ):
    connector_count_test = 0

    def add_connector(loc:cq.Location)->cq.Shape:
        nonlocal connector_count_test
        connector = (
            cq.Workplane("XY")
            .cylinder(2, 11.5)
        )
        
        connector = connector.rotate((1,0,0),(0,0,0),90)
        if connector_count_test == 0:
            connector = connector.translate((0,1,0))
        elif connector_count_test == (max_count-1):
            connector = connector.translate((0,-1,0))
            
        connector_count_test+=1
        return connector.translate((0,0,-0.5)).val().located(loc) #type:ignore
    
    return add_connector

def __add_magnets_with_count(
        shape:cq.Workplane, 
        pip_height:float, 
        max_count:int=2
    ):
    magnet_count_test = 0

    def add_connector( loc:cq.Location)->cq.Shape:
        nonlocal magnet_count_test
        nonlocal shape
        nonlocal pip_height
        
        connector = shape.rotate((1,0,0),(0,0,0),90)
        if magnet_count_test == 0:
            connector = connector.translate((0,pip_height/2,0))
        elif magnet_count_test == (max_count-1):
            connector = connector.translate((0,-1*(pip_height/2),0))
            
        magnet_count_test+=1
        return connector.translate((0,0,-0.5)).val().located(loc) #type:ignore
    
    return add_connector

def __make_curved_connectors(
        radius:float
    ):
    connector_arc =(
        cq.Workplane("XY")
        .polarArray(
            radius  = radius, 
            startAngle  = -90, 
            angle  = 60, 
            count  = 3,
            fill = True,
            rotate = True
        )
        .eachpoint(callback = __add_connector_with_count())
    ).rotate((0,1,0),(0,0,0),90).translate((0,radius,0))
    return connector_arc

def __make_curved_magnets(
        radius:float = 75, 
        pip_height:float = 2.4, 
        pip_radius:float = 1.56
    ):
    pip = (
        cq.Workplane("XY")
        .cylinder(pip_height,pip_radius)
        .rotate((0,1,0),(0,0,0),0)
    )

    x_translate = 10/2 +2
    y_translate = -1*(10/2+6.5)+6+pip_radius/2
    z_translate = 0

    magnet_cuts = (
        cq.Workplane("XY")
        .union(pip.translate((
            -x_translate,
            y_translate,
            z_translate
        )))
        .union(pip.translate((
            x_translate,
            y_translate,
            z_translate
        )))
    )

    magnet_arc =(
        cq.Workplane("XY")
        .polarArray(
            radius  = radius, 
            startAngle  = -90, 
            angle  = 60, 
            count  = 2,
            fill = True,
            rotate = True
        )
        .eachpoint(callback = __add_magnets_with_count(magnet_cuts, pip_height))
    ).rotate((0,1,0),(0,0,0),90).translate((0,radius,0))
    return magnet_arc


def curve(
        radius:float = 75, 
        rotation_angle:float = -30
    ):
    # --- cylinder connectors
    connector_arc = __make_curved_connectors(radius)
    magnet_arc = __make_curved_magnets(radius)

    path = (
        cq.Workplane("ZY")
        .ellipseArc(
            radius,
            radius,
            300,
            rotation_angle=rotation_angle
        )
    )
    #power_face = pipe_face()

    curve_shape = (
        pipe_face()
        #.toPending()
        .sweep(path)
        #.rotate((0,1,0),(0,0,0),90)
        #.translate((x_radius/2,-1*(y_radius/2),0))
    )

    curve_shape_2 = (
        pipe_face()
        #.toPending()
        .sweep(path.rotate((1,0,0),(0,0,0),180))
        #.rotate((0,1,0),(0,0,0),90)
        #.translate((x_radius/2,-1*(y_radius/2),0))
    )

    curve_power_line = (
        cq.Workplane("XY")
        .union(curve_shape)
        .union(connector_arc)
        .cut(magnet_arc)
    ).rotate((0,1,0),(0,0,0),90).translate((0,0,10/2+6.5))

    curve_power_line_2 = (
        cq.Workplane("XY")
        .union(curve_shape_2)
        .cut(curve_shape)
        .union(connector_arc.rotate((0,1,0),(0,0,0),180).rotate((0,0,1),(0,0,0),180))
        .cut(magnet_arc.rotate((0,1,0),(0,0,0),180).rotate((0,0,1),(0,0,0),180))
    ).rotate((0,1,0),(0,0,0),90).translate((0,0,10/2+6.5))

    return curve_power_line, curve_power_line_2
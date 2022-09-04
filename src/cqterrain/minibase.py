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

def __make_magnet_outline(shape_height, magnet_diameter=3, magnet_height=2):
    h_radius = magnet_diameter/2
    h_solid = cq.Workplane("XY").cylinder(magnet_height, h_radius).translate((0,0,(magnet_height/2)-(shape_height/2)))
    return h_solid


def rectangle(length=25, width=25, height=3, taper=-1, magnet_diameter=3, magnet_height=2):
    base = (
        cq.Workplane("XY" )
        .rect(length, width)
        .workplane(offset=height)
        .rect(length+taper, width+taper)
        .loft(combine=True)
        .translate((0,0,-1*(height/2)))
    )

    h_solid = __make_magnet_outline(height, magnet_diameter, magnet_height)

    return cq.Workplane("XY").add(base).cut(h_solid)


def circle(diameter=25, height=3, taper=-1, magnet_diameter=3, magnet_height=2):
    b_base = diameter / 2
    b_top = b_base + taper
    b_solid = cq.Solid.makeCone(b_base, b_top, height).translate((0,0,-1*(height/2)))

    h_solid = __make_magnet_outline(height, magnet_diameter,  magnet_height)
    return cq.Workplane("XY").add(b_solid).cut(h_solid)


def ellipse(x_diameter=52, y_diameter=90, height=3, taper=-1, magnet_diameter=3, magnet_spacing=25, magnet_height=2):
    '''
    @todo should allow for multiple magnets
    '''
    base_x_radius = x_diameter / 2
    base_y_radius = y_diameter / 2

    top_x_radius = base_x_radius + taper
    top_y_radius = base_y_radius + taper

    base = (
        cq.Workplane("XY" )
        .ellipse(base_x_radius,base_y_radius)
        .workplane(offset=height)
        .ellipse(top_x_radius,top_y_radius)
        .loft(combine=True)
        .translate((0,0,-1*(height/2)))
    )

    h_solid = __make_magnet_outline(height, magnet_diameter,  magnet_height)

    #magnet_count = math.floor(y_diameter/ magnet_spacing)
    #magnets = series.make_series(h_solid)
    #log(magnet_count)

    #return h_solid
    return cq.Workplane("XY").add(base).cut(h_solid)


def slot(length=24, width=50, height=3, taper=-1, magnet_diameter=3, magnet_height=2):
    base = (
        cq.Workplane("XY" )
        .slot2D(width, length, 90)
        .workplane(offset=height)
        .slot2D(width+taper, length+taper, 90)
        .loft(combine=True)
        .translate((0,0,-1*(height/2)))
    )
    h_solid = __make_magnet_outline(height, magnet_diameter,  magnet_height)
    return cq.Workplane("XY").add(base).cut(h_solid)

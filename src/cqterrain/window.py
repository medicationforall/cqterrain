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

import cadquery as cq
from cadqueryhelper import grid, shape
import math

def lattice(length=20, width=4, height=40,  tile_size=4, lattice_width=1, lattice_height=1, lattice_angle=45):
    # Determine longest distance between points
    hyp = math.hypot(length, height)
    columns= math.floor(hyp / (tile_size+lattice_width))
    rows= math.floor(hyp / (tile_size+lattice_width))

    # Make a flat plane
    pane = cq.Workplane("XY").box(length, lattice_height, height)

    #make the cutout tile
    tile = cq.Workplane("XY").box(tile_size, lattice_height, tile_size).rotate((1,0,0),(0,0,0),90)
    tiles = grid.make_grid(tile, [tile_size+lattice_width, tile_size+lattice_width], rows=columns, columns=rows).rotate((1,0,0),(0,0,0),-90).rotate((0,1,0),(0,0,0),lattice_angle)
    combine = pane.cut(tiles)
    return combine

def frame(length=20, width = 4, height = 40, frame_width=3):
    outline = cq.Workplane("XY").box(length, width, height)
    inline =  cq.Workplane("XY").box(length-(frame_width*2), width, height-(frame_width*2))
    return outline.cut(inline)

def grill(length=20, width=4, height=40, columns=4, rows=2, grill_width=1, grill_height=1):
    # Make a flat plane
    pane = cq.Workplane("XY").box(length, grill_height, height)
    t_width = length / columns
    t_height = height / rows

    # Make the window cutout
    tile = cq.Workplane("XY").box(t_width, grill_height, t_height).rotate((1,0,0),(0,0,0),90)

    # Repeat the cutout
    tiles = grid.make_grid(tile, [t_width+grill_width, t_height+grill_width], rows=columns, columns=rows).rotate((1,0,0),(0,0,0),-90)

    # Remove the window cutouts leaving the frame
    combine = pane.cut(tiles)
    return combine

def casement(length=20, width=4, height=40, colums=2, rows=3, frame_width=2, grill_width=1, grill_height=1):
    outline = cq.Workplane("XY").box(length, width, height)
    window = frame(length, width, height, frame_width)
    w_grill = grill(length, width, height, colums, rows, grill_width, grill_height)
    return window.add(w_grill)

def industrial(length=20, width=4, height=40, frame_width=4, sphere_radius=1, sphere_top=2, strut_chamfer=.7):
    frame = cq.Workplane("XY").box(length, width, height)
    window = cq.Workplane("XY").box(length-(frame_width*2), width, height)
    combined = frame.cut(window)

    top_spheres = combined.edges("X").translate((0,0,-sphere_top)).sphere(sphere_radius, combine=False)
    bottom_spheres = combined.edges("X").translate((0,0,sphere_top)).sphere(sphere_radius, combine=False)

    combined = combined.edges("X").chamfer(strut_chamfer).cut(top_spheres).cut(bottom_spheres)
    return combined

def cinquefoil(radius=5, sides=5, inner_radius=3, height=2):
    polygon = shape.regular_polygon(radius=radius, sides=sides).translate((0,0,-2.5))
    face = polygon.faces("Z")
    points = face.edges()
    circles = points.cylinder(height,2.6, combine=False)
    center = cq.Workplane("XY").cylinder(height, inner_radius)
    return circles.add(center)

def cinquefoil_frame(outer_radius=7.5, radius=5, sides=5, inner_radius=3, height=2):
    circles = cinquefoil(radius, sides, inner_radius, height)
    frame_circle = cq.Workplane("XY").cylinder(height, outer_radius)
    result = cq.Workplane("XY").add(frame_circle).cut(circles)
    return result

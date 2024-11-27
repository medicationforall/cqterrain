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

def pipe_face(
        radius = 10, 
        side_radius = 1.5, 
        base_height = 1.5, 
        side_a_deg_= 60, 
        side_b_deg = 30, 
        face_rotate = 90
    ):
    
    face = (
        cq.Sketch()
        .push([(0,-radius)])
        .rect(radius,base_height*2)
        .push([(0,0)])
        .circle(radius, mode="a")
        .push([(0,radius)])
        .circle(side_radius, mode="a")
        
    )
    
    side = cq.Workplane("XY").circle(side_radius).extrude(1)
    part:cq.Workplane = (
        cq.Workplane("XY")
        .placeSketch(face)
        .extrude(1)
        .union(side.translate((0,radius,0)).rotate((0,0,1),(0,0,0),-side_a_deg_))
        .union(side.translate((0,radius,0)).rotate((0,0,1),(0,0,0),side_b_deg))
    ).rotate((0,0,1),(0,0,0),face_rotate)
    
    #return part
    return part.faces("<Z").wires().toPending()

def pipe_face_old(
        radius = 10, 
        side_radius = 1.5, 
        base_height = 1.5, 
        side_a_deg_= 60, 
        side_b_deg = 30, 
        face_rotate = 90
    ):
    main = cq.Workplane("XY").circle(radius).extrude(1)
    side = cq.Workplane("XY").circle(side_radius).extrude(1)
    base = cq.Workplane("XY").box(radius,base_height*2,1).translate((0,0,base_height/3))
    outline =  (
        cq.Workplane("XY")
        .union(main)
        .union(side.translate((0,radius,0)))
        .union(side.translate((0,radius,0)).rotate((0,0,1),(0,0,0),-side_a_deg_))
        .union(side.translate((0,radius,0)).rotate((0,0,1),(0,0,0),side_b_deg))
        .union(base.translate((0,-radius,0)))
    ).rotate((0,0,1),(0,0,0),face_rotate)
    return outline.faces("<Z").wires().toPending()
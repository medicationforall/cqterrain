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
from cadqueryhelper import Base

class Hatch(Base):
    def __init__(self):
        self.length:float = 25
        self.width:float = 25
        self.height:float = 4
        self.base_height:float|None = None
        self.base_corner_chamfer:float = 2
        self.base_top_chamfer:float = 2
        self.base_extrude:float = 1.5

        self.hatch_radius:float = 10.5
        self.hatch_height:float = 1.5
        self.hatch_chamfer:float = 0.8
        self.cross_bar_width:float = 4
        self.inner_ring_width:float = 2.5
        self.cut_out_chamfer:float = 0.3

        self.outline:cq.Workplane|None = None
        self.hatch_cut:cq.Workplane|None = None
        self.hatch:cq.Workplane|None  = None
        self.base:cq.Workplane|None = None
        self.hinge:cq.Workplane|None = None

    def make_outline(self):
        outline = (
            cq.Workplane("XY")
            .box(self.length,self.width,self.height)
            .edges("|Z").chamfer(self.base_corner_chamfer)
            )

        self.outline = outline

    def calculate_base_height(self)->float:
        return self.height - self.hatch_height


    def make_base(self):
        base_height = self.calculate_base_height()
        base = (
            cq.Workplane("XY")
            .box(self.length, self.width, base_height)
            .edges("|Z").chamfer(self.base_corner_chamfer)
            .faces("Z").chamfer(self.base_top_chamfer)
            )

        if self.base_extrude >0:
            base = base.faces("-Z").wires().toPending().extrude(self.base_extrude)

        self.base = base.translate((0,0,-1*(self.hatch_height/2)))

    def make_hatch_cut(self):
        base_height = self.calculate_base_height()
        cylinder = (
            cq.Workplane("XY")
            .cylinder(base_height, self.hatch_radius-2)
            .translate((0,0,-1*(self.hatch_height/2)))
        )

        self.hatch_cut = cylinder

    def make_hatch(self):
        cylinder = (
            cq.Workplane("XY")
            .cylinder(self.hatch_height, self.hatch_radius)
            .faces("Z").chamfer(self.hatch_chamfer)
        )

        cut_out = (
            cq.Workplane("XY")
            .cylinder(self.hatch_height/3, self.hatch_radius-self.inner_ring_width)
        )

        cross_bar = (
            cq.Workplane("XY")
            .box((self.hatch_radius-self.inner_ring_width)*2, self.cross_bar_width, self.hatch_height)
            .translate((0,0,0))
        )

        cut_out = (
            cut_out
            .cut(cross_bar)
            .faces("-Z")
            .chamfer(self.cut_out_chamfer)
            .translate((0,0,self.hatch_height/3))

        )

        cut_out_rotated = cut_out.rotate((0,1,0),(0,0,0),180)

        
        base_height = self.calculate_base_height()
        self.hatch = (
            cylinder
            .cut(cut_out)
            .cut(cut_out_rotated)
            .translate((0,0,base_height/2))
        )
        #self.hatch = cut_out_rotated.add(cut_out)

    def make_hinge(self):
        hinge = (
            cq.Workplane("XY")
            .box(4,4,self.hatch_height+1)
            .edges("X")
            .fillet(1)
        )

        cylinder = (
            cq.Workplane("XY")
            .cylinder(4.6 ,.5)
            .rotate((0,1,0),(0,0,0),90)
            .translate((0,1,.4))
        )


        self.hinge = (
            hinge
            .union(cylinder)
            .translate((0,self.hatch_radius,(self.height/2-self.hatch_height/2)-.5))
        )

    def make(self):
        self.make_outline()
        self.make_base()
        self.make_hatch_cut()
        self.make_hatch()
        self.make_hinge()

    def build(self):
        part = (
            cq.Workplane("XY")
            #.union(self.base)
            #.cut(self.hatch_cut)
            #.union(self.hatch)
            #.union(self.hinge)
            #.add(self.outline)
            )
        
        if self.base:
            part = part.union(self.base)

        if self.hatch_cut:
            part = part.cut(self.hatch_cut)

        if self.hatch:
            part = part.union(self.hatch)

        if self.hinge:
            part = part.union(self.hinge)
            
        return part
        #return self.hatch

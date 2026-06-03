# Copyright 2026 James Adams
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
from .make_magnet import make_magnet

class SwivelBase(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.diameter:float = 30
        self.height:float = 6
        self.chamfer:float = 1.5
        self.top_width:float = 2
        self.channel_width:float = 1
        
        self.magnet_diameter:float = 3.2
        self.magnet_height:float = 2.4
        self.cut_height:float|None = None
        
        self.render_greeble:bool = True
        self.greeble_count:int = 6
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.round_base:cq.Workplane|None = None
        self.base_cut:cq.Workplane|None = None
        self.magnet:cq.Workplane|None = None
        self.greebles:cq.Workplane|None = None
        
    def calculate_cut_height(self)->float:
        return self.cut_height if self.cut_height else self.height/2
    
    def calculate_cut_diameter(self)->float:
        diameter = self.diameter - self.top_width*2
        
        if self.chamfer:
            diameter =  diameter - self.chamfer*2
            
        return diameter
        
    def make_outline(self):
        outline = cq.Workplane("XY").cylinder(
            self.height,
            self.diameter/2
        )
        
        self.outline = outline
        
    def make_round_base(self):
        round_base = cq.Workplane("XY").cylinder(
            self.height,
            self.diameter/2
        )
        
        if self.chamfer:
            round_base = round_base.faces("Z").chamfer(self.chamfer)
        
        self.round_base = round_base
        
    def make_base_cut(self):
        diameter = self.calculate_cut_diameter()
            
        #log(f'{diameter=}')
        
        height = self.calculate_cut_height()

        base_cut = cq.Workplane("XY").cylinder(
            height,
            diameter/2
        )
        
        self.base_cut = base_cut
        
    def make_magnet(self):
        magnet = make_magnet(self.magnet_diameter, self.magnet_height)
        
        self.magnet = magnet
        
    def make_greebles(self):
        greeble = (
            cq.Workplane("XY")
            .polygon(6, 7)
            .extrude(self.height)
            .translate((self.diameter/2,0,-self.height/2+self.chamfer))
        )
        
        rotate_degrees = 360 / self.greeble_count
        greebles = cq.Workplane("XY")
        
        for i in range(self.greeble_count):
            greebles = greebles.add(greeble.rotate((0,0,1),(0,0,0),rotate_degrees*i))
        
        
        self.greebles = greebles
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_round_base()
        self.make_base_cut()
        self.make_magnet()
        self.make_greebles()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.round_base:
            part = part.union(self.round_base)
            
        if self.base_cut:
            z_translate = self.height/2 - self.calculate_cut_height()/2
            part = part.cut(self.base_cut.translate((0,0,z_translate)))
            
        if self.magnet:
            #derive based on cut depth
            z_translate = self.height/2 - self.calculate_cut_height() - self.magnet_height/2
            part = part.cut(self.magnet.translate((0,0,z_translate)))
            
        if self.greebles and self.render_greeble:
            part = part.cut(self.greebles)
        
        return part
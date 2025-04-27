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
from . import BaseGreeble
import math
from typing import Literal

class CapGreeble(BaseGreeble):
    def __init__(self):
        super().__init__()
        #properties
        self.length:float = 20
        self.width:float = 8
        self.height:float = 30
        self.top_fillet:float = 2.9
        self.side_fillet:float = 2.5
        self.operation:Literal['chamfer', 'fillet'] = 'chamfer'
        
        self.render_grill:bool = True
        self.grill_height:float = 2
        self.grill_padding_top:float = 1
        self.grill_padding_left:float = 2
        self.grill_margin:float = .5
        
        #shapes
        self.body:cq.Workplane|None = None
        self.grill:cq.Workplane|None = None
        self.grill_internal:cq.Workplane|None = None
        
        self.grill_set:cq.Workplane|None = None
        self.grill_set_internal:cq.Workplane|None = None
        
    def __make_body(self):
        self.body = cq.Workplane('XY').box(
            self.length,
            self.width,
            self.height
        )
        
        if self.operation == 'fillet':
            self.body = self.body.faces("X").edges("Z").fillet(self.side_fillet)
            self.body = self.body.faces("Z").edges("X").fillet(self.side_fillet)
        elif self.operation == 'chamfer':
           self.body = self.body.faces("X").edges("Z").chamfer(self.side_fillet)
           self.body = self.body.faces("Z").edges(">X").chamfer(self.top_fillet)
           self.body = self.body.faces("Z").edges("X").chamfer(self.side_fillet)

    def __make_grill_parts(self):
        grill = cq.Workplane("XY").box(
            self.length - self.grill_padding_left, 
            self.width, 
            self.grill_height
        )
        
        grill_inside = cq.Workplane("XY").box(
            self.length - self.grill_padding_left - self.grill_margin, 
            self.width - self.grill_margin*2, 
            self.grill_height
        )
        self.grill = grill
        self.grill_internal = grill_inside.faces("X").edges("Z").chamfer(1+self.grill_margin*2).translate(((self.grill_margin/2),0,0))

    def __make_grill(self, shape:cq.Workplane):
        grill_height = self.grill_height + self.grill_padding_top*2
        y_count = math.floor(self.height / grill_height) - 1
        
        def add_shape(loc:cq.Location) -> cq.Shape:
            return shape.rotate((1,0,0),(0,0,0),90).val().located(loc) #type: ignore
        
        grill_set = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = 1, 
                ySpacing = grill_height,
                xCount = 1, 
                yCount= y_count, 
                center = True)
            .eachpoint(add_shape)
        ).rotate((1,0,0),(0,0,0),90)
        
        return grill_set
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_body()
        
        if self.render_grill:
            self.__make_grill_parts()

            if self.grill:
                self.grill_set = self.__make_grill(self.grill)

            if self.grill_internal:
                self.grill_set_internal = self.__make_grill(self.grill_internal)
        
    def build(self) -> cq.Workplane:
        super().build()
        scene = cq.Workplane("XY").union(self.body)
        
        if self.render_grill and self.grill_set and self.grill_set_internal:
            scene = (
                scene
                .cut(self.grill_set.translate((self.grill_padding_left/2,0,0)))
                .add(self.grill_set_internal)
            )
        return scene
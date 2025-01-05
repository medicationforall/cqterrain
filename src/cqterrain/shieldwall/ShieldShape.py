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
from . import BaseShape
from typing import Callable

def shield_shape(
    length:float = 20,
    width:float = 20,
    base_height:float = 4,
    middle_width_inset:float = -6,
    travel_distance:float = 2
) -> cq.Workplane:
    base_sPnts = [
        (base_height/2+.00001, width/2),
        (base_height, width/2 - base_height/2 )
    ]
    
    mid_sPnts = [
        (base_height, width/2 + middle_width_inset+travel_distance-0.00001),
        (base_height+2, width/2 + middle_width_inset )
    ]
    
    top_sPnts = [
        (length-travel_distance+0.00001 , width/2 + middle_width_inset),
        (length, width/2 + middle_width_inset -2)
    ]

    result = (
        cq.Workplane("XY")
        .center(-1*(length/2),0)
        .lineTo(0, width/2) # base width
        .lineTo(base_height/2, width/2) #base Height
        .threePointArc(base_sPnts[0], base_sPnts[1])
        .lineTo(base_height, width/2 + middle_width_inset+travel_distance)
        .threePointArc(mid_sPnts[0], mid_sPnts[1])
        .lineTo(length-travel_distance, width/2 + middle_width_inset)
        .threePointArc(top_sPnts[0], top_sPnts[1])
        .lineTo(length, 0)
        .close()
    )
    
    ext = result.extrude(1)
    mirror = (
        cq.Workplane("XY")
        .union(ext.translate((0,0,0-.5)))
        .union(ext.translate((0,0,0-.5)).rotate((1,0,0),(0,0,0),180))
    ).translate((0,0,.5))
    
    mirrored_face_wires = mirror.faces("<Z").wires().toPending()
    return mirrored_face_wires

#-------------------------

class ShieldShape(BaseShape):
    def __init__(self):
        super().__init__()
        
        # parameters
        self.length:float = 20
        self.width:float = 20
        self.base_height:float = 5.6
        self.middle_width_inset:float = -6
        self.travel_distance:float = 2
        self.shape_method:Callable[[float, float, float, float, float], cq.Workplane] = shield_shape
        
        # shapes
        self.shape:cq.Workplane|None = None
        
    def _make_shape(self):
        self.shape = self.shape_method(
            self.length,
            self.width,
            self.base_height,
            self.middle_width_inset,
            self.travel_distance
        )
        
    def make(self, parent = None):
        super().make(parent)
        self._make_shape()
        
    def build(self) -> cq.Workplane:
        super().build()
        if self.shape:
            return self.shape
        else:
            raise Exception("Unable to resolve SheildShape shape")
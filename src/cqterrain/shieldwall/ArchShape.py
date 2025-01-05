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

def arch_pointed(
        length:float = 30, 
        height:float = 50, 
        inner_height:float = 25
    ) -> cq.Workplane:
    m_length = length/2 #mirror length
    sPnts = [
        (inner_height+.00001, m_length+0),
        (height, 0)
    ]

    result = (
        cq.Workplane("XY")
        .center(-(height/2),0)
        .lineTo(0, m_length)
        .lineTo(inner_height, m_length)
        .spline(sPnts, includeCurrent=True)
        .close().mirrorX()
    )
    return result


class ArchShape(BaseShape):
    def __init__(self):
        super().__init__()
        
        #properties
        self.length:float = 25
        self.width:float = 20
        self.base_height:float = 5
        self.middle_width_inset:float = -6
        
        #shapes
        self.shape:cq.Workplane|None = None
        
    def make(self, parent=None):
        super().make(parent)
        self.shape = arch_pointed(
          length=self.width,
          height=self.length,
          inner_height=self.base_height
        )
        
    def build(self) -> cq.Workplane:
        super().build()
        if self.shape:
            return self.shape
        else:
            raise Exception("Unable to resolve ArchShape shape")
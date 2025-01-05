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
from cadqueryhelper import Base

class BaseCut(Base):
    def __init__(self):
        super().__init__()
        
        #properties
        self.length:float = 75
        self.width:float = 10
        self.height:float = 4
        self.angle:float = 30
        
        #shapes
        self.cut_out:cq.Workplane|None = None
        
    def __make_cut_out(self):
        angle = 90 - self.angle
        self.cut_out = (
            cq.Workplane("XY")
            .sketch()
            .trapezoid(self.width,self.height,angle)
            .finalize()
            .extrude(self.length)
            .translate((0,0,-1*(self.length/2)))
            .rotate((1,0,0),(0,0,0),-90)
            .rotate((0,0,1),(0,0,0),-90)
        )
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_cut_out()
        
        
    def build(self) -> cq.Workplane:
        super().build()

        if self.cut_out:
            return self.cut_out
        else:
            raise Exception("Unable to resolve BaseCut cut_out")
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
from . import BaseStraight, BaseRamp

class Bridge(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.straight_count:int = 2
        self.width:float = 75*2
        self.height:float = 50
        
        #blueprints
        self.bp_straight:BaseStraight = BaseStraight()
        self.bp_ramp:BaseRamp = BaseRamp()
        
    def make(self, parent=None):
        super().make(parent)
        self.bp_straight.width = self.width
        self.bp_straight.height = self.height
        self.bp_straight.make()
        
        self.bp_ramp.width = self.width
        self.bp_ramp.height = self.height
        self.bp_ramp.make()
    
    def build(self)->cq.Workplane:
        super().build()
        straight:cq.Workplane = self.bp_straight.build()
        ramp:cq.Workplane = self.bp_ramp.build()
        
        s_length = self.bp_straight.length * self.straight_count
        r_length = self.bp_ramp.length
        
        straight_sections = cq.Workplane("XY")
        
        if self.straight_count>0:
            for index in range(0,self.straight_count):
                 straight_sections = straight_sections.add(straight.translate((self.bp_straight.length*index,0,0)))
        
        scene = (
            cq.Workplane("XY")
            .add(ramp.translate((
                s_length/2+r_length/2,
                0,
                0
            )).rotate((0,0,1),(0,0,0),180))
            .add(straight_sections.translate((-s_length/2+self.bp_straight.length/2,0,0)))
            .add(ramp.translate((
                s_length/2+r_length/2,
                0,
                0
            )))
        )
        
        return scene
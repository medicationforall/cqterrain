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

class BaseRamp(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.length:float = 75*2
        self.width:float = 75*2
        self.height:float = 50
        
        #shapes
        self.ramp:cq.Workplane|None = None
        
    def make(self, parent=None):
        super().make(parent)
        pts = [
            (0,0),
            (self.length,0),
            (0,self.height)
        ]
        self.ramp = (
            cq.Workplane("XZ").polyline(pts).close().extrude(self.width)
        ).translate((-self.length/2,self.width/2,-self.height/2))
        
    def build(self)->cq.Workplane:
        super().build()
        if self.ramp:
            return self.ramp
        else:
            raise Exception('Unable to resolve bridge ramp')
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


class BaseStraight(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.length:float = 75*2
        self.width:float = 75*2
        self.height:float = 50
        
        #shapes
        self.straight:cq.Workplane|None = None
        
    def make(self, parent=None):
        super().make(parent)
        self.straight = (
            cq.Workplane("XY").box(
                self.length,
                self.width,
                self.height
            )
        )
        
    def build(self)->cq.Workplane:
        super().build()
        if self.straight:
            return self.straight
        else:
            raise Exception('unable to resolve straight bridge section')
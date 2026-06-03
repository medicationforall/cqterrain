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

class SwivelTop(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.diameter:float = 30
        self.height:float = 3
        
        self.magnet_diameter:float = 3.2
        self.magnet_height:float = 2.4
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.magnet:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").cylinder(
            self.height,
            self.diameter/2
        )
        
        self.outline = outline
        
    def make_top(self):
        top_base = cq.Workplane("XY").cylinder(
            self.height,
            self.diameter/2
        )
        
        self.top_base = top_base
        
    def make_magnet(self):
        magnet = make_magnet(self.magnet_diameter, self.magnet_height)
        
        self.magnet = magnet
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_top()
        self.make_magnet()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.top_base:
            z_translate = self.height/2
            part = part.add(self.top_base.translate((0,0,z_translate)))
            
        if self.magnet:
            z_translate = self.magnet_height/2
            part = part.cut(self.magnet.translate((0,0,z_translate)))
        
        return part
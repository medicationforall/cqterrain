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
from cadqueryhelper.shape import ring

class FanHousing(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.diameter:float = 10
        self.height:float = 5
        
        #housing
        self.housing_inner_diameter:float = 2
        self.housing_wall_cut_width:float = 1
        self.housing_wall_height:float = 1
        self.housing_wall_chamfer:float = 0.499
        
        #fin
        self.render_fins:bool = True
        self.fin_length:float = 0.5
        self.fin_width:float = 0.5
        self.fin_count:int = 3
        
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.housing:cq.Workplane|None = None
        self.fins:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.diameter,
            self.diameter,
            self.height
        )
        
        self.outline = outline
        
    def make_housing(self):
        housing = ring(
            diameter = self.diameter,
            inner_diameter = self.diameter - self.housing_inner_diameter,
            height = self.height
        )
        
        inner_height = self.height - self.housing_wall_height
        
        housing_wall_cut = ring(
            diameter = self.diameter,
            inner_diameter = self.diameter - self.housing_wall_cut_width,
            height = inner_height
        )
        
        if self.housing_wall_chamfer:
            housing_wall_cut = housing_wall_cut.faces("<Z").edges()[1].chamfer(self.housing_wall_chamfer)
            housing_wall_cut = housing_wall_cut.faces(">Z").edges()[1].chamfer(self.housing_wall_chamfer)
        
        self.housing = housing.cut(housing_wall_cut)
        
    def make_fins(self):
        fin_rotate = 360 / self.fin_count
        inner_height = self.height - self.housing_wall_height
        
        fin = (
            cq.Workplane("XY")
            .box(self.fin_length, self.fin_width, inner_height)
            .translate(((self.diameter/2)-self.fin_length/2,0,0))
        )
        
        fins = cq.Workplane("XY")
        
        for i in range(self.fin_count):
            fins = fins.add(fin.rotate((0,0,1),(0,0,0),fin_rotate*i))
            
        self.fins = fins
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_housing()
        self.make_fins()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.housing:
            part = part.add(self.housing)
            
        if self.render_fins and self.fins:
           part = part.union(self.fins)
        
        return part
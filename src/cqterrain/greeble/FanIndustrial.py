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
from . import FanHousing, FanBlade

class FanIndustrial(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 30
        self.width:float = 25
        self.height:float = 20
        
        self.diameter:float = 40
        
        #housing parameters
        self.housing_inner_diameter:float = 4
        self.fan_cylinder_diameter:float = 10
        self.fin_width:float = 1.5
        self.fin_length:float = 1.5
        self.fin_count:int = 6
        self.housing_wall_cut_width:float = 2
        self.housing_wall_height:float = 3
        
        self.blade_count:int = 14
        self.shift_rotate:float = 10
        self.blade_width:float = 3
        self.blade_rotate:float = 25
        
        # blueprints
        self.bp_housing:Base = FanHousing()
        self.bp_fan:Base = FanBlade()
        
        #shapes
        self.outline:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_housing(self):
        bp_house = self.bp_housing
        bp_house.housing_wall_cut_width = self.housing_wall_cut_width
        bp_house.housing_wall_height = self.housing_wall_height
        bp_house.fin_width = self.fin_width
        bp_house.fin_length = self.fin_length
        bp_house.fin_count = self.fin_count
        bp_house.housing_inner_diameter = self.housing_inner_diameter
        bp_house.diameter = self.diameter
        bp_house.height = self.height
        
        self.bp_housing.make()
        
    def make_fan(self):
        bp_fan = self.bp_fan
        bp_fan.diameter = self.diameter - self.housing_inner_diameter
        bp_fan.cylinder_diameter = self.fan_cylinder_diameter
        bp_fan.cylinder_height = self.height
        
        bp_fan.blade_width = self.blade_width
        bp_fan.blade_rotate = self.blade_rotate
        bp_fan.blade_count = self.blade_count
        bp_fan.debug = False
        bp_fan.shift_rotate = self.shift_rotate
        bp_fan.shift_translate = 0
        
        bp_fan.make()
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_housing()
        self.make_fan()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bp_housing:
            housing = self.bp_housing.build()
            housing_height = self.bp_housing.height
            part = part.add(housing.translate((0,0,housing_height/2)))
            
        if self.bp_fan:
            fan = self.bp_fan.build()
            part = part.add(fan)
        
        return part
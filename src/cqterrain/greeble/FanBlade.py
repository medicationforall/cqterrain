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


class FanBlade(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.diameter:float = 15
        self.height:float = 5
        
        self.cylinder_height:float = 2.5
        self.cylinder_diameter:float = 5
        
        self.blade_width:float = 1
        self.blade_rotate:float = 23
        self.blade_count:int = 3
        self.debug:bool = False
        self.shift_rotate:float = 10
        self.shift_translate:float = .5
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.spindle:cq.Workplane|None = None
        self.blade:cq.Workplane|None = None
        self.blades:cq.Workplane|None = None
        
    def make_outline(self):
        height = self.cylinder_height + self.cylinder_diameter/2
        outline = cq.Workplane("XY").cylinder(
            height,
            self.diameter/2
        ).translate((0,0,height/2))
        
        self.outline = outline
        
    def make_spindle(self):
        cylinder_height = self.cylinder_height
        spindle = cq.Workplane("XY").cylinder(cylinder_height,self.cylinder_diameter/2)
        bell = cq.Workplane("XY").sphere(self.cylinder_diameter/2)
        
        self.spindle = (
            spindle
            .union(bell.translate((0,0,cylinder_height/2)))
            .translate((0,0,cylinder_height/2))
        )
        
    def make_blade(self):
        length = self.diameter/2
        width = self.blade_width
        height = self.cylinder_height
        blade = (
            cq.Workplane("XY")
            .box(length, width, height)
            .rotate((1,0,0),(0,0,0),self.blade_rotate)
            .translate((length/2,0,height/2))
            
        )
        
        self.blade = blade.intersect(self.outline)
        
    def make_blades(self):
        repeat_rotate = 360 / self.blade_count
        blades = cq.Workplane("XY")
        for i in range(self.blade_count):
            blades = blades.add(self.blade.rotate((0,0,1),(0,0,0),repeat_rotate*i))
            
        self.blades = blades
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_spindle()
        self.make_blade()
        self.make_blades()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.spindle:
            part = part.add(self.spindle)
            
        if self.blades:
            blade_rotate = 360 / self.blade_count
            
            if not self.debug:
                blades = (
                    cq.Workplane("XY")
                    .union(self.blades)
                    .translate((0,0,self.shift_translate))
                    .intersect(self.blades.rotate((0,0,1),(0,0,0),self.shift_rotate))
                )
                
                part = part.union(blades)
            else:
                blades = (
                    cq.Workplane("XY")
                    .union(self.blades)
                    .translate((0,0,self.shift_translate))
                    .add(self.blades.rotate((0,0,1),(0,0,0),self.shift_rotate))
                )
                
                part = part.add(blades)
        
        return part
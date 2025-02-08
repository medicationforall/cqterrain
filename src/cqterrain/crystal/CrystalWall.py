# Copyright 2025 James Adams
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
from cqterrain.minibase import slot_uneven
from cqterrain.crystal import crystal_random
import random
from numpy import arange

def resolve_range_val(v)->float|int:
    if type(v) == tuple:
        range_values = arange(v[0],v[1]+v[2],v[2])
        v = random.choice(range_values)
        
    return v

class CrystalWall(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.length:float = 75
        self.width:float = 25
        self.height:tuple[float,float,float]|float = (20,30,2.5)
        
        self.seed:str = 'test'
        self.crystal_count:int = 5
        self.crystal_margin:float = 10

        self.render_base:bool = True
        self.base_height:float = 3
        self.base_taper:float = -1
        self.base_render_magnet:bool = False
        self.base_detail_height:float = 3
        self.base_uneven_height:float = 4
        self.base_peak_count:tuple[int,int]|int = (9,10)

        self.render_crystals:bool = True
        self.crystal_base_width:tuple[float,float,float]|float = 20.0
        self.crystal_base_height:tuple[float,float,float]|float = 0.5
        self.crystal_inset_width:tuple[float,float,float]|float = 20.0
        self.crystal_inset_height:tuple[float,float,float]|float = (1.0,3.0,0.5)
        self.crystal_mid_height:tuple[float,float,float]|float = (2.0,5.0,0.5)
        self.crystal_mid_width:tuple[float,float,float]|float = (10,20.0,2.5)
        self.crystal_top_height:tuple[float,float,float]|float = (10,15,2.5)
        self.crystal_top_width:tuple[float,float,float]|float = (10,15.0,2.5)
        self.crystal_faces:tuple[int,int,int]|int=(5,10,1)
        self.crystal_intersect:bool = True

        self.random_rotate_x:tuple[float,float,float]|float|None = (-20.0, 20.0, 2.5)
        self.random_rotate_y:tuple[float,float,float]|float|None = (-15.0, 15.0, 2.5)
        
        #shapes
        self.crystals = None
        self.mini_base = None
        self.base_cut = None
        
    def make_mini_base(self):
        self.mini_base = slot_uneven(
            length = self.length,
            width = self.width,
            base_height = self.base_height,
            seed = self.seed,
            taper = self.base_taper,
            render_magnet = self.base_render_magnet,  
            magnet_diameter = 3, 
            magnet_height = 2,
            detail_height = self.base_detail_height,
            uneven_height = self.base_uneven_height,
            peak_count = (9,10),
            segments= 6
        )

    def calculate_height(self)->float:
        height = self.height
        if type(self.height) == tuple:
            height = self.height[1]
        return height #type:ignore
        
    def crystal_adder(self):
        # closure
        count = 0
        def add_crystal(loc:cq.Location)->cq.Shape:
            nonlocal count
            count += 1
            adder_seed = f"{self.seed}_{count}"
            #log(f'{adder_seed}')
            crystal,height = crystal_random(
                height = self.height,
                seed = adder_seed,
                base_width = self.crystal_base_width,
                base_height = self.crystal_base_height,
                inset_width = self.crystal_inset_width,
                inset_height = self.crystal_inset_height,
                mid_height = self.crystal_mid_height,
                mid_width = self.crystal_mid_width,
                top_height = self.crystal_top_height,
                top_width = self.crystal_top_width,
                faces=self.crystal_faces,#min,max,step
                intersect = self.crystal_intersect
            )
            crystal = crystal.translate((0,0,height/2))
            
            if self.random_rotate_x:
                random_rotate_x = resolve_range_val(self.random_rotate_x)
                #log(f'{random_rotate_x}')
                crystal = crystal.rotate((1,0,0),(0,0,0),random_rotate_x)
                
            if self.random_rotate_y:
                random_rotate_y = resolve_range_val(self.random_rotate_y)
                #log(f'{random_rotate_y}')
                crystal = crystal.rotate((0,1,0),(0,0,0),random_rotate_y)
                
            
            return crystal.val().located(loc) #type:ignore
        return add_crystal
        
    def make_crystals(self):
        x_spacing = (self.length - self.crystal_margin * 2) / self.crystal_count
        group = (
            cq.Workplane("XY")
            .rarray(
            xSpacing = x_spacing, 
            ySpacing = self.width,
            xCount = self.crystal_count, 
            yCount= 1,
            center = True)
            .eachpoint(callback = self.crystal_adder())
        )
        
        self.crystals = group
        
    def make_base_cut(self):
        height = self.calculate_height()

        self.base_cut = (
            cq.Workplane("XY").box(
                self.length,
                self.width,
                height #type:ignore
            )
        )
    
    def make(self, parent=None):
        super().make(parent)
        
        if self.render_crystals:
            self.make_crystals()
        
        if self.render_base:
            self.make_mini_base()
            
        self.make_base_cut()
        
    def build(self):
        super().build()
        scene = cq.Workplane("XY")#.box(10,10,10)
        
        if self.render_crystals and self.crystals:
            scene = scene.union(self.crystals)
        
        if self.render_base and self.mini_base:
            scene = scene.union(self.mini_base.translate((0,0,self.base_height/2)))
            
        if self.base_cut:
            height = self.calculate_height()
            scene= scene.cut(self.base_cut.translate((0,0,-height/2)))
            
        return scene
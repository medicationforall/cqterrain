# Copyright 2023 James Adams
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

class IndustrialStairs(Base):
    def __init__(
            self,
            length:float = 75,
            width:float = 75,
            height:float = 75,
            stair_count:int = 9,
            stair_chamfer:float|None = None,
            render_step_cut:bool = True,
            render_hollow:bool = True,
            cut_padding:float = 4
        ):
        super().__init__()
        # parameters
        self.length:float = length
        self.width:float = width
        self.height:float = height

        self.stair_count:int = stair_count
        self.stair_chamfer:float|None = stair_chamfer
        
        self.render_step_cut:float = render_step_cut
        self.cut_padding:float = cut_padding
        self.render_hollow:bool = render_hollow

        #parts
        self.stairs:cq.Workplane|None = None

    def __make_step(self, i, stair_interval_lengh, stair_interval_height):
        step = cq.Workplane("XY").box(
            stair_interval_lengh,
            self.width, 
            stair_interval_height*(i+1)
        )
        
        if self.render_step_cut:
            cut_out = cq.Workplane("XY").box(
                stair_interval_lengh,
                (self.width)-self.cut_padding, 
                stair_interval_height-2
            ).faces("Z").edges("X").chamfer(2)
            
            #return cut_out
            cut_z_translate = ((stair_interval_height/2)*(i))-1
            step = step.cut(cut_out.translate((0,0,cut_z_translate)))
            
        if self.render_hollow and i > 1:
            shell = cq.Workplane("XY").box(
                stair_interval_lengh,
                self.width-6, 
                stair_interval_height*(i-1)
            ).translate((0,0,-stair_interval_height-1))
            step = step.cut(shell)
            
        return step#.translate((0,5*i,1+i))

    def __make_stairs(self):
        stair_length = self.length
        stair_interval_length = stair_length / self.stair_count
        stair_interval_height = self.height / self.stair_count
        
        stairs =(
            cq.Workplane("XY")
        )
        
        for i in range(self.stair_count):
            step = self.__make_step(
                i, 
                stair_interval_length,
                stair_interval_height
            )
            
            if self.stair_chamfer:
                step = step.faces("<Y").edges("Z").chamfer(self.stair_chamfer)
                
            stairs = stairs.union(
                step.translate((
                    stair_length-(stair_interval_length/2)-stair_interval_length*i,
                    0,
                    -1*(self.height/2)+(stair_interval_height*(i+1)/2)
                )))
            
        self.stairs = stairs.translate((-1*(stair_length/2),0,0))

    def make(self, parent=None):
        super().make(parent)
        self.__make_stairs()

    def build(self):
        super().build()
        scene = (
            cq.Workplane("XY")
        )

        if self.stairs:
            scene = scene.union(self.stairs)
        return scene
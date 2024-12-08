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

class Spool(Base):
    def __init__(
            self,
            height:float = 60,
            radius:float = 80,
            cut_radius:float = 30,
            wall_width:float = 3,
            internal_wall_width:float = 3,
            internal_z_translate:float = 0
        ):
        super().__init__()
        #parameters
        self.height:float = height
        self.radius:float = radius
        self.cut_radius:float = cut_radius
        self.wall_width:float = wall_width
        self.internal_wall_width:float = internal_wall_width
        self.internal_z_translate:float = internal_z_translate
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.cut_hole:cq.Workplane|None = None
        self.cut_wall:cq.Workplane|None = None
        
    def __make_outline(self):
        self.outline = (
            cq.Workplane("XY")
            .cylinder(
                self.height,
                self.radius
            )
        )
        
    def __make_cut_hole(self):
        self.cut_hole = (
            cq.Workplane("XY")
            .cylinder(
                self.height,
                self.cut_radius
            )
        )
        
    def __make_cut_wall(self):
        internal_cut = (
            cq.Workplane("XY")
            .cylinder(
                self.height-self.wall_width*2,
                self.cut_radius+(self.internal_wall_width)
            )
        )
        
        self.cut_wall = (
            cq.Workplane("XY")
            .cylinder(
                self.height-self.wall_width*2,
                self.radius
            )
        )
        
        self.cut_wall = self.cut_wall.cut(internal_cut)
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_outline()
        self.__make_cut_hole()
        self.__make_cut_wall()
        
    def build(self):
        super().build()
        scene = (cq.Workplane("XY"))

        if self.outline:
            scene = scene.union(self.outline)

        if self.cut_hole:
            scene = scene.cut(self.cut_hole)

        if self.cut_wall:
            scene = (
                scene
                .cut(self.cut_wall)
                .cut(self.cut_wall.translate((
                    0,
                    0,
                    self.internal_z_translate
                )))  
            )

        return scene
    
    def build_no_center(self, ):
        super().build()
        scene = (
            cq.Workplane("XY")
            .union(self.outline)        
        )

        if self.outline:
            scene = scene.union(self.outline)

        if self.cut_wall:
            scene = (
                scene
                .cut(self.cut_wall)
                .cut(self.cut_wall.translate((
                    0,
                    0,
                    self.internal_z_translate
                )))  
            )
        return scene

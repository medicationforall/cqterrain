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
from . import BaseMesh
import math

class Mesh(BaseMesh):
    def __init__(self):
        super().__init__()
        #properties
        self.length:float = 75
        self.width:float = 3
        self.height:float = 25
        
        self.tile_length:float = 5
        self.tile_width:float = 5
        self.tile_padding:float = 0.2
        self.tile_chamfer:float = 1.4
        
        #shapes
        self.tile:cq.Workplane|None = None
        self.tiles:cq.Workplane|None = None
        self.outline:cq.Workplane|None = None
        
    def __make_outline(self):
        self.outline = (
            cq.Workplane('XY')
            .box(self.length,self.height, self.width/2)
        )
        
    def _make_tile(self):
        self.tile = (
            cq.Workplane('XY')
            .box(
                self.tile_length,
                self.tile_width,
                self.width/2
            )
            .faces("-Z")
            .chamfer(self.tile_chamfer)
        )
        
    def _make_tiles(self):
        tile_length = self.tile_length + self.tile_padding * 2
        tile_width = self.tile_width + self.tile_padding * 2
        
        x_count = math.floor(self.length / tile_length)
        y_count = math.floor(self.height / tile_width)
        
        #log(f'{y_count=}')
        
        def add_star(loc:cq.Location) -> cq.Shape:
            return self.tile.val().located(loc) # type: ignore
        
        self.tiles = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = tile_length, 
                ySpacing = tile_width,
                xCount = x_count, 
                yCount= y_count, 
                center = True)
            .eachpoint(callback = add_star)
        )
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_outline()
        self._make_tile()
        self._make_tiles()
        
    def build(self) -> cq.Workplane:
        super().build()

        if self.tiles:
            mesh = (
                cq.Workplane('XY')
                .union(self.outline)
                #.cut(self.tile)
                .cut(self.tiles)
            ).rotate((1,0,0),(0,0,0),-90).translate((0,-1*(self.width/4),0))
            
            scene = (
                cq.Workplane("XY")
                .union(mesh) #front
                .union(mesh.rotate((0,0,1),(0,0,0),180)) #back
            )

            return scene
        else:
            raise Exception('Unable to resolve Mesh tiles')
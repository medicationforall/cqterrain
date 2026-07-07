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

class BricksLayered(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 30
        self.width:float = 25
        self.height:float = 60
        
        self.rows:int = 4
        self.columns:int = 3
        self.layers:int = 5
        self.spacing:float = .7
        self.spacing_z:float = 0
        self.tile_padding:float = 2
        
        #shapes
        self.bricks = None
        
    def make(self):
        super().make()
        self.make_bricks()
        
    def make_bricks(self):
        x_spacing = (self.length+self.tile_padding)/self.columns
        y_spacing = (self.width+self.tile_padding)/self.rows
        z_spacing = (self.height+self.tile_padding)/self.layers
        length = x_spacing - self.spacing
        width = y_spacing - self.spacing
        height = z_spacing - self.spacing
        tile = cq.Workplane("XY").box(length, width, height)
        
        def add_tile(loc:cq.Location) ->cq.Shape:
            return tile.val().located(loc) #type:ignore
        
        tiles = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = x_spacing, 
                ySpacing = y_spacing,
                xCount = self.columns+1, 
                yCount= self.rows+1, 
                center = True)
            .eachpoint(add_tile)
        )
        
        tile_layers = cq.Workplane("XY")
        
        for i in range(self.layers):
            x_translate = x_spacing/2 * (i%2==0)
            y_translate = y_spacing/2 * (i%2==0)
            tile_layers = tile_layers.union(tiles.translate((
                x_translate,
                y_translate,
                z_spacing*i
            )))
        
        tile_layers = tile_layers.translate((0,0,height/2))#-(self.height+self.tile_padding)))
        self.bricks = tile_layers
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bricks:
            part = part.add(self.bricks)
        
        return part
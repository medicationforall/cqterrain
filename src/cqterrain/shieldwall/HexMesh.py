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
import math
from . import Mesh

class HexMesh(Mesh):
    def __init__(self):
        super().__init__()

    def build_hex_key(self):
        tile = (
            cq.Workplane('XY')
            .polygon(6, self.tile_length-0.6)
        ).extrude(30)

        return tile
        
    def _make_tile(self):
        tile = (
            cq.Workplane('XY')
            .polygon(6, self.tile_length)
        ).extrude(self.width/2).translate((0,0,-1*(self.width/4)))
        
        self.tile = tile.faces("-Z").chamfer(self.tile_chamfer)
        
    def _make_tiles(self):
        tile_length = self.tile_length - self.tile_padding
        tile_width = self.tile_length + self.tile_padding * 2
        
        x_count = math.floor(self.length / tile_length)
        y_count = math.floor(self.height / tile_width)+2
        
        cell_count = 0
        column_count = 0
        def add_tile(loc:cq.Location) -> cq.Shape:
            nonlocal cell_count
            nonlocal column_count
            
            location = loc.toTuple() 
            new_loc = location[0]
            
            if cell_count % y_count == 0:
                column_count+=1
                
            if column_count % 2 == 0:
                # log('even column')
                pass
            else:
                # log('odd column')
                new_loc = (location[0][0], location[0][1]+self.tile_length/2, location[0][2])
                
            cell_count+=1
            
            return self.tile.translate(new_loc).val() #type: ignore
        
        tiles = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = tile_length, 
                ySpacing = tile_width,
                xCount = x_count, 
                yCount= y_count, 
                center = True)
            .eachpoint(callback = add_tile)
        )
        
        if self.outline:
            self.tiles = tiles.intersect(self.outline)
        
    def build(self) -> cq.Workplane:
        #super().build()
        if self.tiles:
            mesh = (
                cq.Workplane('XY')
                .union(self.outline)
                #.add(self.tile)
                .cut(self.tiles)
            ).rotate((1,0,0),(0,0,0),-90).translate((0,-1*(self.width/4),0))
            
            scene = (
                cq.Workplane("XY")
                .union(mesh)
                .union(
                    mesh
                    .rotate((0,0,1),(0,0,0),180)
                    .rotate((0,1,0),(0,0,0),180)
                )
            )

            return scene
        else:
            raise Exception('Unable to resolve HexMesh tiles')
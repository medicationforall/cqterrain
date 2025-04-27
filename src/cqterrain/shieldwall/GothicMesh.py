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
from cadqueryhelper import shape
from . import Mesh
import math

class GothicMesh(Mesh):
    def __init__(self):
        super().__init__()
        self.tile_length:float = 10
        self.tile_padding:float = 0
        self.arch_frame_width:float = 1.5
        self.side_length:float|None = None
        
    def _make_tile(self):
        tile_width = self.width /2

        tile_plate = (
            cq.Workplane('XY')
            .box(self.tile_length,tile_width/2,self.height)
        )
        
        arch = shape.arch_pointed(
          length=self.tile_length,
          width=tile_width/2,
          height=self.height,
          inner_height=self.height/3
        )
        
        arch_inner = shape.arch_pointed(
          length=self.tile_length - self.arch_frame_width ,
          width=tile_width/2,
          height=self.height - self.arch_frame_width *2,
          inner_height=self.height/3 - self.arch_frame_width *2
        )
        
        circle = (
            cq.Workplane('XY')
            .cylinder(tile_width/2, self.tile_length/2-self.arch_frame_width/2)
            .rotate((1,0,0),(0,0,0),90)
        )
        
        inner_circle_radius = self.tile_length/2-self.arch_frame_width
        
        inner_circle = (
            cq.Workplane('XY')
            .cylinder(tile_width/2, inner_circle_radius)
            .rotate((1,0,0),(0,0,0),90)
        )
        
        cut_circle = (
            cq.Workplane('XY')
            .cylinder(tile_width, inner_circle_radius/2.5)
            .rotate((1,0,0),(0,0,0),90)
        )
        
        cut_circle_offset = cut_circle.translate((0,0,inner_circle_radius/2))
        
        cut_circles = (
            cq.Workplane("XY")
            .union(cut_circle)
            .union(cut_circle_offset)
            .union(cut_circle_offset.rotate((0,1,0),(0,0,0),90))
            .union(cut_circle_offset.rotate((0,1,0),(0,0,0),180))
            .union(cut_circle_offset.rotate((0,1,0),(0,0,0),-90))
        )
    
        tile = (
            cq.Workplane("XY")
            .union(tile_plate.translate((0,(tile_width/4),0)))
            .union(arch.translate((0,-(tile_width/4),0)))
            .cut(arch_inner.translate((0,-(tile_width/4),0)))
            .union(circle.translate((0,-(tile_width/4),0)))
            .cut(inner_circle.translate((0,-(tile_width/4),0)))
            .cut(cut_circles)
        )
        
        self.tile = tile
        
    def _make_tiles(self):
        tile_length = self.tile_length + self.tile_padding * 2
        tile_width = self.width
        
        x_count = math.floor(self.length / tile_length)
        y_count = 1
        
        self.side_length = self.length - (tile_length * x_count) 
        self.side = cq.Workplane('XY').box(self.side_length, self.width, self.height)
        
        def add_tile(loc:cq.Location) -> cq.Shape:
            return self.tile.val().located(loc) #type: ignore
        
        self.tiles = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = tile_length, 
                ySpacing = 10,
                xCount = x_count, 
                yCount= y_count, 
                center = True)
            .eachpoint(add_tile)
        )
    
    def build(self) -> cq.Workplane:
        if self.tiles:
            scene = (
                cq.Workplane("XY")
                .union(self.tiles.translate((0,-(self.width/4),0)))
                .union(self.tiles.rotate((0,0,1),(0,0,0), 180).translate((0,(self.width/4),0)))
                .union(self.side.translate((self.length/2,0,0)))
                .union(self.side.translate((-(self.length/2),0,0)))
            )
            return scene
        else:
            raise Exception('Unable to resolve GothicMesh tiles')
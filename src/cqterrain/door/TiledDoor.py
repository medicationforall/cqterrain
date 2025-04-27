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
from cadqueryhelper import Base
from ..greeble import gothic_one
from . import pull_handle
from typing import Callable

class TiledDoor(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.length:float = 30
        self.width:float = 3
        self.height:float = 40
        
        self.render_tiles:bool=True
        self.tiles_x_count:int = 2
        self.tiles_y_count:int = 3
        self.tile_x_padding:float = 3
        self.tile_y_padding:float = 2
        self.tile_width_padding:float = .5
        
        self.render_handle:bool=True
        self.handle_length:float = 3
        self.handle_width_padding:float = .25
        self.handle_height:float = 6
        self.handle_x_margin:float = .5
        self.handle_mirrored:bool  = False
        self.handle_handle_length:float = 1
        self.handle_base_chamfer:float = 1
        
        #method callbacks
        self.tile_bp:Callable[[float, float, float], cq.Workplane] = gothic_one
        self.handle_bp:Callable[[float, float, float, float, float, bool], cq.Workplane] = pull_handle
        
        #shapes
        self.outline:cq.Workplane|None = None
        
        self.tile:cq.Workplane|None = None
        self.cut_tile:cq.Workplane|None = None
        
        self.tiles:cq.Workplane|None = None
        self.cut_tiles:cq.Workplane|None = None
        
        self.handle:cq.Workplane|None = None
        self.cut_handle:cq.Workplane|None = None
        
    def __make_outline(self):
        self.outline = (
            cq.Workplane("XY")
            .box(
                self.length, 
                self.width, 
                self.height
            )
        )
        
    def __make_tile(self):
        self.tile = (
            self.tile_bp(
                self.length/self.tiles_x_count - (self.tile_x_padding*2), 
                self.width + (self.tile_width_padding*2), 
                self.height/self.tiles_y_count - (self.tile_y_padding*2)
            ).rotate((1,0,0),(0,0,0),90)
        )
        
        self.cut_tile = (
            cq.Workplane("XY")
            .box(
                self.length/self.tiles_x_count - (self.tile_x_padding*2), 
                self.width + (self.tile_width_padding*2), 
                self.height/self.tiles_y_count - (self.tile_y_padding*2)
            ).rotate((1,0,0),(0,0,0),90)
        )
        
    def __make_tiles(self):
        x_spacing = self.length / self.tiles_x_count
        y_spacing = self.height / self.tiles_y_count
        
        def add_tile(loc:cq.Location) -> cq.Shape:
            return self.tile.val().located(loc) #type: ignore

        tiles = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = x_spacing, 
                ySpacing = y_spacing,
                xCount = self.tiles_x_count, 
                yCount= self.tiles_y_count, 
                center = True)
            .eachpoint(add_tile)
        )
        
        self.tiles = tiles.rotate((1,0,0),(0,0,0),-90)
        
    def __make_cut_tiles(self):
        x_spacing = self.length / self.tiles_x_count
        y_spacing = self.height / self.tiles_y_count
        
        def add_cut_tile(loc:cq.Location) -> cq.Shape:
            return self.cut_tile.val().located(loc) #type: ignore

        cut_tiles = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = x_spacing, 
                ySpacing = y_spacing,
                xCount = self.tiles_x_count, 
                yCount= self.tiles_y_count, 
                center = True)
            .eachpoint(add_cut_tile)
        )
        
        self.cut_tiles = cut_tiles.rotate((1,0,0),(0,0,0),-90)
        
    def __make_handle(self):
        self.handle = self.handle_bp(
            length = self.handle_length,
            width = self.width + self.handle_width_padding*2,
            height =self.handle_height,
            handle_length = self.handle_handle_length,
            handle_base_chamfer = self.handle_base_chamfer,
            mirrored = self.handle_mirrored
        )
        
        self.cut_handle = (
            cq.Workplane("XY").box(
                self.handle_length,
                self.width + (self.tile_width_padding*2),
                self.handle_height
            )
        )
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_outline()
        
        if self.render_tiles:
            self.__make_tile()
            self.__make_cut_tiles()
            self.__make_tiles()
        
        if self.render_handle:
            self.__make_handle()
        
    def build(self) -> cq.Workplane:
        super().build()
        handle_x_translate = (self.length/2) - (self.handle_length /2) - self.handle_x_margin
        handle_y_translate = (self.handle_height/2)
        scene = (
            cq.Workplane()
            .union(self.outline)
        )
        
        if self.render_tiles and self.tiles and self.cut_tiles:
            scene = (
                scene
                #.add(self.tile)
                #.cut(self.cut_tile)
                .cut(self.cut_tiles)
                .union(self.tiles)
            )
            
            if self.render_handle and self.handle and self.cut_handle:
                scene = (
                    scene
                    .cut(self.cut_handle.translate((
                        -handle_x_translate,
                        0,
                        -handle_y_translate))
                    )
                    .union(self.handle.translate((
                        -handle_x_translate,
                        0,
                        -handle_y_translate))
                    )
                )
        return scene
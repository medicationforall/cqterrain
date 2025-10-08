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
from typing import Literal

class HeavyDoor(Base):
    def __init__(self):
        super()
        #parameters
        self.length:float = 30 
        self.width:float =  3
        self.height:float = 45
        self.trim_size:float = 1.5
        self.inset_depth:float = 1
        
        self.render_side_cuts:bool = True
        
        self.side_cut_height:float = 20 
        self.side_cut_length:float = 5
        self.side_cut_distance:float = 5
        self.side_cut_operation:Literal['chamfer','fillet']|None = 'chamfer'
        
        self.render_cross_bars:bool = True
        self.cross_bars_angle:float = 30
        self.cross_bar_offset:float = 8
        self.cross_bar_height:float|None = None
        
        self.render_window:float = True
        self.window_height:float = 15
        self.window_width:float = 8
        self.window_trim:float|None = None
        self.window_offset:float = 8
        
        self.render_window_pane_cut:bool = True
        self.window_pane_margin:float = 0.4
        self.window_pane_width:float = 0.4
        self.window_key_width:float = 2
        self.window_key_margin:float = 0.2
        self.wndow_key_text:str = "Heavy Door Window Key"
        
        self.render_cross_section:bool = False

        #shapes
        self.body = None
        self.side_cut = None
        self.inset = None
        self.cross_bars = None
        self.window = None
        self.window_cut = None
        self.window_key = None
        
        
    def make_body(self):
        self.body = cq.Workplane("XY").box(self.length, self.width, self.height)
        
    def make_side_cut(self):
        
        if self.side_cut_distance > self.side_cut_length:
            raise Exception(f"side_cut_distance {self.side_cut_distance} can not be greater than side_cut_length {self.side_cut_length}")
        
        self.side_cut = (
            cq.Workplane("XY")
            .box(self.side_cut_length, self.width, self.side_cut_height)
        )
        
        if self.side_cut_operation == 'fillet':
            self.side_cut = (
                self.side_cut
                .faces("Z")
                .edges(">X")
                .fillet(self.side_cut_distance-.000001)
            )
            
        if self.side_cut_operation == 'chamfer':
            self.side_cut = (
                self.side_cut
                .faces("Z")
                .edges(">X")
                .chamfer(self.side_cut_distance-.000001)
            )
            
        self.body = (
            self.body
            .cut(self.side_cut.translate((
                -self.length/2+self.side_cut_length/2,
                0,
                -self.height/2+self.side_cut_height/2
            )))
            .cut(self.side_cut.translate((
                -self.length/2+self.side_cut_length/2,
                0,
                -self.height/2+self.side_cut_height/2
            )).rotate((0,0,1),(0,0,0),180))
        )
        
    def make_cross_bar(self):
        cross_bar_height = self.height
        
        if self.cross_bar_height:
            cross_bar_height = self.cross_bar_height
        cross_bar = (
            cq.Workplane("XY")
            .box(self.trim_size, self.inset_depth, cross_bar_height)
        )
        
        cross_bars = (
            cq.Workplane("XY")
            .union(cross_bar.rotate((0,1,0),(0,0,0),self.cross_bars_angle))
            .union(cross_bar.rotate((0,1,0),(0,0,0),-self.cross_bars_angle))
        ).translate((0,0,self.cross_bar_offset))
        
        self.cross_bars = cross_bars.intersect(self.body)
        
        
    def make_inset(self):
        self.body = (
            self.body
            .rotate((1,0,0),(0,0,0),90)
            .tag("body")
            .faces("Z")
            .edges()
            .toPending()
            .offset2D(-self.trim_size)
            .extrude(-self.inset_depth, combine="cut")
            .faces("-Z",tag="body")
            .edges()
            .toPending()
            .offset2D(-self.trim_size)
            .extrude(self.inset_depth, combine="cut")
            .rotate((1,0,0),(0,0,0),-90)
        )
        
    def calculate_trim_size(self):
        trim_size = self.trim_size
        
        if self.window_trim:
            trim_size = self.window_trim
        return trim_size
        
        
    def make_window(self):
        window_outline = (
            cq.Workplane("XY")
            .slot2D(self.window_height, self.window_width)
            .extrude(self.width)
            .translate((0,0,-self.width/2))
        )
        
        trim_size = self.calculate_trim_size()
        
        window_cut = (
            cq.Workplane("XY")
            .slot2D(self.window_height-trim_size*2, self.window_width-trim_size*2)
            .extrude(self.width)
            .translate((0,0,-self.width/2))
        )
        
        self.window = window_outline.rotate((0,0,1),(0,0,0),90).rotate((1,0,0),(0,0,0),90)
        self.window_cut = window_cut.rotate((0,0,1),(0,0,0),90).rotate((1,0,0),(0,0,0),90)
        
    def calculate_window_pane_height(self):
        trim_size = self.calculate_trim_size()
        return self.height/2 + self.window_height - self.window_height/2-trim_size + self.window_pane_margin + self.window_offset
        
    def make_window_pane(self):
        trim_size = self.calculate_trim_size()
        
        self.window_pane = (
            cq.Workplane("XY")
            .box(
                self.window_width + self.window_pane_margin*2 - trim_size*2,
                self.window_pane_width,
                self.calculate_window_pane_height()
            )
        )
        
        self.window_key = (
            cq.Workplane("XY")
            .box(
                self.window_width + self.window_key_margin*2 - trim_size*2,
                self.window_key_width,
                self.calculate_window_pane_height()
            )
            .add(cq.Workplane("XY").text(self.wndow_key_text,3.2,1).rotate((0,0,1),(0,0,0),90).rotate((1,0,0),(0,0,0),90).translate((0,self.window_key_width/2,0)))
        )
        
    def make(self, parent=None):
        super().make(parent)
        self.make_body()
        
        self.make_cross_bar()
        
        if self.render_side_cuts:
            self.make_side_cut()
        
        if self.render_cross_bars:
            self.make_cross_bar()
            
        self.make_inset()
        
        if self.render_window:
            self.make_window()
            
        self.make_window_pane()
            
    def build_door(self):
        door = (
            cq.Workplane("XY")
            .union(self.body)
        )
        
        if self.render_cross_bars:
            door = (
                door
                .union(self.cross_bars.translate((0,self.width/2 - self.inset_depth/2,0)))
                .union(self.cross_bars.translate((0,-(self.width/2 - self.inset_depth/2),0)))

            )
            
        if self.render_window:
            door = (
                door
                .union(self.window.translate((0,0,self.window_offset)))
                .cut(self.window_cut.translate((0,0,self.window_offset)))
            )
            
        if self.render_window_pane_cut:
            door = door.cut(self.window_pane.translate((0,0,-self.height/2+self.calculate_window_pane_height()/2)))
        else:
            door = door.add(self.window_pane.translate((0,0,-self.height/2+self.calculate_window_pane_height()/2)))
        
        if self.render_cross_section:
            cross_section = (
                cq.Workplane("XY")
                .box(self.length, self.width, self.height)
                .translate((0,-self.width/2,0))
            )
            
            door = door.cut(cross_section)
            
        #door = door.faces(">Y").edges()
        return door
        
    def build(self):
        super().build()
        door = self.build_door()
        return door
    
    def build_plate(self):
        door = self.build_door()
        plate = (
            cq.Workplane("XY")
            .union(door.translate((0,self.width/2,0)))
        )
        
        if self.render_window_pane_cut:
            key = self.window_key
            plate = plate.add(key.translate((self.length/2+10,self.window_key_width/2,0)))
            
        return plate.rotate((1,0,0),(0,0,0),-90)
# Copyright 2022 James Adams
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
from cadqueryhelper.grid import series

class BlastDoor(Base):
    def __init__(self):
        super().__init__()
        self.length:float = 25
        self.width:float = 5
        self.height:float = 32
        self.fillet:float = 3
        self.chamfer:float = .6

        self.bar_height:float = 3
        self.bar_width:float = 1
        self.bar_margin_z:float = 5
        self.bar_margin_x:float = 1.5
        self.bar_cap_length:float = 3

        self.handle_height:float = 1.5
        self.handle_radius:float = 4
        self.handle_rotation:float = -15

        self.outline:cq.Workplane|None = None
        self.door:cq.Workplane|None = None
        self.locking_bars:cq.Workplane|None = None
        self.handles:cq.Workplane|None = None

    def make_door(self):
        outline = (
            cq.Workplane("XY")
            .box(self.length, self.width, self.height)
            .edges("|Y").fillet(self.fillet)
        )
        self.outline = outline
        self.door = (cq.Workplane("XY").add(outline))
        if self.chamfer:
            self.door = self.door.chamfer(self.chamfer)

    def make_locking_bar(self):
        bar = cq.Workplane("XY").box(self.length-self.bar_margin_x-self.bar_cap_length,self.bar_width,self.bar_height)
        bar = bar.faces("X or -X").box(self.bar_cap_length, self.bar_width+1, self.bar_height+1)
        return bar

    def make_locking_bars(self):
        bar = self.make_locking_bar()

        offset=self.height-self.bar_height*2- self.bar_margin_z*2
        bars = series(bar, 2, height_offset =offset)

        y_plus = cq.Workplane("XY").add(bars).translate((0,self.width/2+self.bar_width/2,0))
        y_minus = cq.Workplane("XY").add(bars).translate((0,-1*(self.width/2+self.bar_width/2),0))
        result =  cq.Workplane("XY").add(y_plus).add(y_minus)

        self.locking_bars = result

    def make_handle(self):
        '''
        @todo too many hard coded values
        '''
        outline = cq.Workplane("XY").cylinder(self.handle_height,self.handle_radius)
        interior_cut = cq.Workplane("XY").cylinder(self.handle_height,self.handle_radius-1.5)
        center = cq.Workplane("XY").cylinder(self.handle_height,1).rotate((1,0,0),(0,0,0),90).faces("-Y").fillet(.3)
        spoke = cq.Workplane("XY").box(self.handle_radius*2-1, 1, 1).faces("Y or -Y").fillet(.4)
        handle = (
            cq.Workplane("XY")
            .union(outline)
            .cut(interior_cut)
            .rotate((1,0,0),(0,0,0),90)
            .fillet(.5)
            .union(center)
            .union(spoke)
            .union(spoke.rotate((0,1,0),(0,0,0),90))
        )
        handle = handle
        return handle

    def make_handles(self):
        handle = self.make_handle()
        y_plus = handle.rotate((0,0,1),(0,0,0),180).rotate((0,1,0),(0,0,0),self.handle_rotation).translate((0,self.width/2+self.handle_height/2,0))
        y_minus = handle.rotate((0,1,0),(0,0,0),self.handle_rotation).translate((0,-1*(self.width/2+self.handle_height/2),0))
        self.handles = y_plus.add(y_minus)

    def make(self):
        self.make_door()
        self.make_locking_bars()
        self.make_handles()

    def build(self) -> cq.Workplane:
        door = (
            cq.Workplane("XY")
            .union(self.door)
            .union(self.locking_bars)
            .union(self.handles)
        )
        return door

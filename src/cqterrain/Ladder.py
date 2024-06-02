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
from cadqueryhelper import series, Base
import math
from typing import Callable

def _make_side_rail(
        width:float, 
        height:float, 
        rail_width:float
    ) -> cq.Workplane:
    rail = (cq.Workplane("XY")
            .box(height, rail_width, width)
            .rotate((0,0,1),(0,0,0),90)
            .rotate((1,0,0),(0,0,0),90)
            )
    return rail

def _make_rung(
        length:float, 
        width:float, 
        height:float
    ) ->cq.Workplane:
    rung = cq.Workplane("XY").box(length, width ,height)
    return rung

class Ladder(Base):
    def __init__(self, 
            length:float = 25, 
            width:float = 4, 
            height:float = 50, 
            rail_width:float = 2
        ):
        self.length = length
        self.width = width
        self.height = height
        self.rail_width = rail_width
        self.rung_height:float = 2
        self.rung_width:float = 2
        self.rung_padding:float = 6

        # callbacks
        self.make_rung:Callable[[float,float,float],cq.Workplane] = _make_rung
        self.make_side_rail:Callable[[float,float,float],cq.Workplane] = _make_side_rail

        # parts
        self.outline:cq.Workplane|None = None
        self.side_rails:list[cq.Workplane] = []
        self.rung:cq.Workplane|None = None
        self.rungs:cq.Workplane|None = None

    def make(self):
        self.outline = cq.Workplane("XY").box(
            self.length, 
            self.width, 
            self.height
        )
        self.__make_rails()
        self.__make_rung()
        self.__make_rungs()

    def __make_rung(self):
        self.rung = self.make_rung(self.length, self.rung_width, self.rung_height)

    def __make_rungs(self):
        rung_count:int = math.floor(self.height / (self.rung_height + self.rung_padding))
        if not self.rung:
            raise Exception('self.rung is empty')

        self.rungs = series(self.rung, rung_count, height_offset=0 + self.rung_padding)

    def __make_rails(self):
        side_rail_left = self.make_side_rail(self.width, self.height, self.rail_width)
        side_rail_left = side_rail_left.translate((-1*(self.length/2)+(self.rail_width/2),0,0))

        side_rail_right = self.make_side_rail(self.width, self.height, self.rail_width)
        side_rail_right = side_rail_right.translate(((self.length/2)-(self.rail_width/2),0,0))

        self.side_rails.append(side_rail_left)
        self.side_rails.append(side_rail_right)

    def build(self):
        combined = (cq.Workplane("XY")
        .union(self.side_rails[0])
        .union(self.side_rails[1])
        .union(self.rungs)
        )

        return combined

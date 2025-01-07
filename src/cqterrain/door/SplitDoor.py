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
from cadqueryhelper import Base, shape, wave

class SplitDoor(Base):
    def __init__(self):
        super().__init__()
        self.length:float = 25
        self.width:float = 2
        self.height:float = 40
        self.base_height:float = 20
        self.open:float = 0
        self.bar_height:float = 1
        self.chamfer_minus:float = 0.1

        self.cut_door:cq.Workplane|None = None
        self.split_door:cq.Workplane|None = None

    def __make_cut_door(self):
        cut_door = shape.arch_pointed(
            self.length,
            self.width,
            self.height,
            self.base_height
        )
        self.cut_door = cut_door

    def __make_door(self):
        divide = .8
        left_wave = wave.square(self.height, self.length/2+divide, self.width, 5, self.length/2-divide)

        # for making the clean cut
        door_left = (
            left_wave
            .rotate((1,0,0),(0,0,0),-90)
            .rotate((0,1,0),(0,0,0),90)
            .translate((self.length/4-divide/2,0,0))

        )

        door_left_chamfer = (
            left_wave
            .rotate((1,0,0),(0,0,0),-90)
            .rotate((0,1,0),(0,0,0),90)
            .faces("<X").edges("Z")
            .chamfer(self.width/2-self.chamfer_minus)
            .translate((self.length/4-divide/2,0,0))

        )

        left = (cq.Workplane("XY"))

        if self.cut_door:
            left = left.union(self.cut_door).intersect(door_left_chamfer)

        right = (
            cq.Workplane("XY")
        )

        if self.cut_door:
            right = (
                right
                .add(self.cut_door)
                .cut(door_left)
                .faces(">X").edges("Z")
                .chamfer(self.width/2-self.chamfer_minus)
            )

        bar = (
            cq.Workplane("XY").box(self.length, self.width, self.bar_height)
            .translate((0,0,-1*(self.height/2-self.bar_height/2)))
        )

        scene = (
            cq.Workplane("XY")
            .union(left.translate((self.open,0,0)))
            .union(right.translate((-self.open,0,0)))
            .union(bar)
        )

        if self.cut_door:
            scene_cut = self.cut_door.intersect(scene)
            self.split_door = scene_cut


    def make(self):
        super().make()
        self.__make_cut_door()
        self.__make_door()

    def build(self)->cq.Workplane:
        super().build()
        scene = cq.Workplane("XY")
    
        if self.split_door:
            scene.add(self.split_door)
        else:
            raise Exception("Unable to resolve split door")
        return scene

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

def _cut_slot(
        shape, 
        size
    ):
    chamfer_size = size*.4
    height = shape.val().BoundingBox().zlen
    slots = shape.faces("|Y").box(size, size, height, combine=False)
    slots = slots.edges("Z").chamfer(chamfer_size)
    return shape.cut(slots)

def _inner_door(
        length, 
        width, 
        height
    ):
    door = cq.Workplane("XY").box(length, width, height)
    door = _cut_slot(door, 1.5)
    return door

def _outer_frame(
        outline, 
        length, 
        frame_length, 
        width, 
        height, frame_height
    ):
    frame_cut = cq.Workplane("XY").box(length-frame_length, width, height - frame_height).translate((0,0,-1*(frame_height/2)))
    frame = outline.cut(frame_cut)
    return frame

class Door:
    def __init__(
            self, 
            length:float = 25, 
            width:float = 8, 
            frame_length:float = 3, 
            frame_height:float = 4, 
            inner_width:float = 3, 
            height:float  = 40, 
            x_offset:float = 0
        ):
        # parameters
        self.length:float = length
        self.width:float = width
        self.frame_length:float = frame_length
        self.frame_height:float = frame_height
        self.inner_width:float = inner_width
        self.height:float = height
        self.x_offset:float = x_offset

        #parts
        self.outline:cq.Workplane|None = None
        self.inner_door:cq.Workplane|None = None
        self.frame:cq.Workplane|None = None

    def make_outline(self):
        self.outline = cq.Workplane("XY").box(self.length, self.width, self.height)

    def make_out_frame(self):
        frame = _outer_frame(self.outline, self.length, self.frame_length, self.width, self.height, self.frame_height)
        self.frame = frame.chamfer(.7)

    def make_inner_door(self):
        self.inner_door = (
            _inner_door(self.length-self.frame_length, self.inner_width, self.height - self.frame_height)
            .translate((0,0,-1*(self.frame_height/2)))
         )

    def make(self):
        self.make_outline()
        self.make_out_frame()
        self.make_inner_door()

    def build(self):
        combined = cq.Workplane("XY")

        if self.frame and self.inner_door:
            combined = (
                combined
                .union(self.frame)
                .union(self.inner_door)
            )

        if self.outline:
            # why am I doing this?
            self.outline = self.outline.translate((self.x_offset,0,0))

        return combined.translate((self.x_offset,0,0))

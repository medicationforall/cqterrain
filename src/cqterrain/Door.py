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

def _cut_slot(shape, size):
    chamfer_size = size*.4
    height = shape.val().BoundingBox().zlen
    slots = shape.faces("|Y").box(size, size, height, combine=False)
    slots = slots.edges("Z").chamfer(chamfer_size)
    return shape.cut(slots)

def _inner_door(length, width, height):
    door = cq.Workplane("XY").box(length, width, height)
    door = _cut_slot(door, 1.5)
    return door

def _outer_frame(outline, length, frame_length, width, height, frame_height):
    frame_cut = cq.Workplane("XY").box(length-frame_length, width, height - frame_height).translate((0,0,-1*(frame_height/2)))
    frame = outline.cut(frame_cut)
    return frame

class Door:
    def __init__(self, length=25, width=8, frame_length=3, frame_height=4, inner_width=3, height=40, x_offset=0):
        self.length=length
        self.width=width
        self.frame_length=frame_length
        self.frame_height=frame_height
        self.inner_width=inner_width
        self.height=height
        self.x_offset=x_offset

        self.outline=None
        self.inner_door=None
        self.frame=None


    def make(self):
        self.outline = cq.Workplane("XY").box(self.length, self.width, self.height)

        frame = _outer_frame(self.outline, self.length, self.frame_length, self.width, self.height, self.frame_height)
        self.frame = frame.chamfer(.7)
        self.inner_door = (_inner_door(self.length-self.frame_length, self.inner_width, self.height - self.frame_height)
            .translate((0,0,-1*(self.frame_height/2)))
            )
        self.outline = self.outline.translate((self.x_offset,0,0))

    def build(self):
        combined = self.frame.union(self.inner_door)
        return combined.translate((self.x_offset,0,0))

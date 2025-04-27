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

def __make_pipe(
        length:float, 
        radius:float
    ) -> cq.Workplane:
    inner_cable = (
        cq.Workplane("XY")
        .cylinder(length, radius)
    ).rotate((0,1,0),(0,0,0),90)
    return inner_cable

def __make_segments(
        length:float, 
        segment_length:float, 
        space:float, 
        segment:cq.Workplane
    ) -> cq.Workplane:
    count = math.floor(length / (segment_length + space))

    def __add_segment(loc:cq.Location) -> cq.Shape:
        return segment.val().located(loc) #type:ignore

    if not count:
        count = 1

    segments = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = space+segment_length, 
            ySpacing = space+segment_length,
            xCount = count, 
            yCount= 1, 
            center = True)
        .eachpoint(__add_segment)
    )
    
    return segments

def corrugated_straight(
    length:float = 50,
    radius:float = 5,
    inner_radius:float = 3,
    segment_length:float = 5,
    space:float = 5
) -> cq.Workplane:    
    inner_pipe = __make_pipe(length,inner_radius)
    segment = __make_pipe(segment_length, radius)
    segments = __make_segments(length, segment_length, space, segment)
    
    return inner_pipe.union(segments)
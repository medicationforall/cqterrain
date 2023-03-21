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

import cadquery as cq

def support(length=10, width=10, height=30, inner_height=8, inner_length=4, inner_width=4, top_offset=0):
    result = (cq.Workplane("XY")
          .box(length, width, inner_height)
          .wires(">Z")
          .toPending()
          .workplane(offset=height-inner_height).center(0,(width/2)-(inner_width/2)+(top_offset*-1))
          .rect(inner_length, inner_width)
          .loft(combine=True)
          )

    #zero out result
    result = result.translate((0,0,inner_height/2))
    # center column
    result = result.translate((0,0,-1*(height/2)))
    return result

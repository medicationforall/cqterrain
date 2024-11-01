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
import random
import math

def make_stones(
        parts:list[cq.Workplane], 
        dim:list[float] = [5,5,2], 
        rows:int = 2, 
        columns:int = 5,
        seed:str|None = "test4"
    ) -> cq.Workplane:
    grid = cq.Workplane("XY")
    
    if seed:
        random.seed(seed)

    # loop the rows
    for row_i in range(rows):
        row_offset = (dim[0] * row_i)
        # loop the columns per row
        for col_i in range(columns):
            col_offset = (dim[1] * col_i)

            col_push_x = 0
            col_push_y = 0
            if col_i % 2 == 1:
                col_push_x = 0
                col_push_y = 0

            z_push = random.randrange(-1*math.floor(dim[2]),math.floor(dim[2]))
            z_push=0
            # move the part in a random direction along the x and y axis.
            x_rand = random.randrange(-1*(math.floor(dim[0]/2)),(math.floor(dim[0]/2)))
            y_rand = random.randrange(-1*(math.floor(dim[1]/2)),(math.floor(dim[1]/2)))

            # choose a random part from the parts list
            part = random.choice(parts)

            # add the part to the assembly
            grid = grid.union(
                part
                .translate((
                    row_offset + col_push_x + x_rand, 
                    col_offset + col_push_y + y_rand, 
                    z_push
                ))
            )

    length = dim[1] * columns
    width = dim[0] * rows

    work = cq.Workplane("XZ").center(0, 0).workplane()
    work.add(grid)

    # zero out the grid
    work = work.translate(((dim[0]/2),(dim[1]/2)))
    work = work.translate((-1*(width/2),-1*(length/2)))
    return work

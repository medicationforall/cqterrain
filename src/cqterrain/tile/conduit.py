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
from .. import pipe as terrain_pipe
import math

def conduit(
        length:float = 25, # length of the tile
        width:float = 25, # with of the tile
        height:float = 4, # height of the tile
        frame:float = 1, # size of the frame can be 0
        frame_depth:float =3, # depth of the frame that the pipe is set into, can be zero
        pipe_count:int|None = None, # hard coded pipe count. If falsy the pipes count will be determined by the witdth of the tile and the diameter of the pipe.
        
        radius:float = 4, # radius of the pipe
        inner_radius:float = 3, # internal radius of the inner pope
        segment_length:float = 6, # size of the pipe segments
        space:float = 4, # space between the pipe segments
        
        pipe_padding:float = 1 # padding between pipes
    ) -> cq.Workplane:
    
    tile = cq.Workplane("XY")
    outline = cq.Workplane("XY").box(length, width, height)

    tile = tile.union(outline)
    
    if frame and frame_depth:
        frame_box = cq.Workplane("XY").box(length-frame*2, width-frame*2, frame_depth)
        tile = tile.cut(frame_box.translate((0,0,height/2-frame_depth/2)))

    tile_pipe = terrain_pipe.corrugated_straight(
        (length-frame*2), 
        radius, 
        inner_radius, 
        segment_length, 
        space
    )
    
    pipe_cut = cq.Workplane("XY").box(length, radius*2, radius*2)
    
    half_pipe = (
        cq.Workplane("XY")
        .union(tile_pipe)
        .cut(pipe_cut.translate((0,0,-radius)))
    )
    
    if not pipe_count:
        pipe_count = math.floor((width-frame*2)/(radius*2+pipe_padding*2))
        #log(f'pipe count {pipe_count}')
        
    # if pipe_count is still falsy skip adding pipes altogether.
    if pipe_count:
        def __add_pipe(loc:cq.Location)->cq.Shape:
            return half_pipe.val().located(loc) #type:ignore
        
        half_pipes = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = radius*2, 
                ySpacing = radius*2+pipe_padding*2,
                xCount = 1, 
                yCount= pipe_count, 
                center = True)
            .eachpoint(callback = __add_pipe)
        )

        tile = tile.union(half_pipes.translate((0,0,height/2-frame_depth)))

    return tile
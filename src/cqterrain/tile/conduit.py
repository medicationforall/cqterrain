import cadquery as cq
from .. import pipe as terrain_pipe
import math

def conduit(
        length = 25, # length of the tile
        width = 25, # with of the tile
        height = 4, # height of the tile
        frame= 1, # size of the frame can be 0
        frame_depth =3, # depth of the frame that the pipe is set into, can be zero
        pipe_count = None, # hard coded pipe count. If falsy the pipes count will be determined by the witdth of the tile and the diameter of the pipe.
        
        radius = 4, # radius of the pipe
        inner_radius = 3, # internal radius of the inner pope
        segment_length = 6, # size of the pipe segments
        space = 4, # space between the pipe segments
        
        pipe_padding = 1 # padding between pipes
    ):
    
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
        def __add_pipe(loc):
            return half_pipe.val().located(loc)
        
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
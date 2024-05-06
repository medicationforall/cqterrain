import cadquery as cq
from cqterrain import tile

result = tile.conduit(
    length = 25, # length of the tile
    width = 25, # with of the tile
    height = 4, # height of the tile
    frame= 1, # size of the frame can be 0
    frame_depth =3, # depth of the frame that the pipe is set into, can be zero
    pipe_count = None, # hard coded pipe count. If falsy the pipes count will be determined by the witdth of the tile and the diameter of the pipe.
    
    radius = 4, # radius of the pipe
    inner_radius = 3, # internal radius of the inner pope
    segment_length = 6, # size of the pipe segments
    space = 4, # spece between the pipe segments
    
    pipe_padding = 1 # padding between pipes
)
#show_object(result)

cq.exporters.export(result,'stl/tile_conduit.stl')
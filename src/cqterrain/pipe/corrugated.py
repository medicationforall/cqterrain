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
        .eachpoint(callback = __add_segment)
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
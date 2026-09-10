import cadquery as cq
from cadqueryhelper import wave


def corrugated(
    length:float = 25,
    width:float = 25,
    height:float = 3,
    segment_length:float = 4,
    inner_width:float = 0.5
):

    result = wave.sine(
        length = length,
        width = height,
        height = width,
        segment_length = segment_length,
        inner_width = inner_width
    ).rotate((1,0,0),(0,0,0),-90)
    
    return result
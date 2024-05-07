import cadquery as cq
from cadqueryhelper import wave

def vent(
        length:float = 25,
        width:float = 25,
        height:float = 4,
        segment_length:float = 3,
        inner_width:float = 2,
        frame_width:float = 2,
        chamfer:float|None = None,
        wave_pattern = wave.sawtooth 
    ) -> cq.Workplane:

    sawtooth = wave_pattern(
        length = length-frame_width,
        width = height,
        height = width-frame_width,
        segment_length = segment_length,
        inner_width = inner_width
    ).rotate((1,0,0),(0,0,0),-90)

    outline = cq.Workplane("XY").box(length,width,height)
    inline = cq.Workplane("XY").box(
        length-frame_width,
        width-frame_width,
        height
    )

    frame = outline.cut(inline)
    if chamfer:
        frame = frame.faces("X or -X").edges("Z").chamfer(chamfer)

    return frame.union(sawtooth)#.add(inline)

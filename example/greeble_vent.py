import cadquery as cq
from cqterrain import greeble

vent = greeble.vent(
    length = 25,
    width = 25,
    height = 4,
    segment_length = 3,
    inner_width = 2,
    frame_width = 2,
    chamfer = None
)

cq.exporters.export(vent,'stl/greeble_vent.stl')

import cadquery as cq
from cqterrain.segment import BaseSegment

bp_segment = BaseSegment()

bp_segment.length = 75
bp_segment.width = 75
bp_segment.height = 75
bp_segment.floor_height = 6
bp_segment.wall_width = 4

bp_segment.make()

ex_segment = bp_segment.build()

#show_object(ex_segment)

cq.exporters.export(ex_segment,'stl/segment_base_segment.stl')
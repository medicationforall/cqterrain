import cadquery as cq
from cqterrain import pipe

result = pipe.corrugated_straight(
    length = 50,
    radius = 4,
    inner_radius = 3,
    segment_length = 6,
    space = 4
)
#show_object(result)
cq.exporters.export(result,'out/pipe_corrugated.stl')
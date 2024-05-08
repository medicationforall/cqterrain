import cadquery as cq
from cqterrain import greeble

result = greeble.spoked_wheel(
    radius = 10,
    height = 2,
    frame = 2,
    inner_radius = 3,
    spoke_width = 2,
    spoke_height = 1.5,
    spoke_fillet = .5,
    spoke_count = 12,
    frame_chamfer = .5,
    inner_chamfer = .5
)

cq.exporters.export(result,'stl/greeble_spoked_wheel.stl')
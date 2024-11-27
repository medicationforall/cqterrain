import cadquery as cq
from cqterrain import pipe

curve1, curve2 =  pipe.curve()

cq.exporters.export(curve1,"stl/pipe_curve_left.stl")
cq.exporters.export(curve2,"stl/pipe_curve_right.stl")
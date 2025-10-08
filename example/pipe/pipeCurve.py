import cadquery as cq
from cqterrain import pipe

curve1, curve2 =  pipe.curve(
    radius = 75, 
    rotation_angle = -30
)

#show_object(curve1)
#show_object(curve2)

cq.exporters.export(curve1,"stl/pipe_curve_left.stl")
cq.exporters.export(curve2,"stl/pipe_curve_right.stl")
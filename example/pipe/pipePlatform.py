import cadquery as cq
from cqterrain import pipe

ex_platform = pipe.platform()

#show_object(ex_platform)
cq.exporters.export(ex_platform,"stl/pipe_platform_pipe.stl")
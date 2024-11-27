import cadquery as cq
from cqterrain import pipe

end_cap = pipe.end()


#show_object(end_cap)
cq.exporters.export(end_cap,"stl/pipe_end.stl")
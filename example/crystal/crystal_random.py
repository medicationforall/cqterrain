import cadquery as cq
from cqterrain.crystal import crystal_random

ex_crystal,ex_height = crystal_random(
    height = (50,80,2.5),#min,max,step
    base_width = 20.0,
    base_height = 0.5,
    inset_width = 25.0,
    inset_height = 3.1,
    mid_height = (2.0,10.0,0.5),
    mid_width = (20,35.0,2.5),
    top_height = (20,40,5),
    top_width = (20,35.0,2.5),
    faces=(5,10,2),#min,max,step
    seed='purple',
    intersect = True
)

# show_object(model)
cq.exporters.export(ex_crystal,'stl/crystal_random.stl')
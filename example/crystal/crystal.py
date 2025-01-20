import cadquery as cq
from cqterrain import obelisk

model = obelisk(
        base_width=20.0,
        base_height=0.5,
        inset_width=25.0,
        inset_height=3.1,
        mid_width=25.0,
        mid_height=2.0,
        top_width=35.0,
        top_height=40.0,
        height=70.0,
        faces=7,
        intersect=True
    ).rotate((0,0,1),(0,0,0),0)

# show_object(model)
cq.exporters.export(model,'stl/crystal.stl')
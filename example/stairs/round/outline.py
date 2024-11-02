import cadquery as cq
from cqterrain.stairs.round import outline

outline_ex = outline(
    height = 75,
    inner_diameter = 75,
    diameter = 75 + 55,
    rotate = 50
).rotate((0,0,1),(0,0,0),45/2)

#show_object(outline_ex)

cq.exporters.export(outline_ex,'stl/stairs_round_outline.stl')
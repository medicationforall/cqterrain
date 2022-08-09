import cadquery as cq
from cqterrain import stairs
#from cadqueryhelper import shape

#cone = shape.cone()
#cube = shape.cube()
#cylinder = shape.cylinder(12, 20)

f = stairs.make_stairs(
    length = 30,
    width = 10,
    height = 30,
    run = 5,
    stair_length_offset = 0,
    stair_height = 1,
    rail_width = 1,
    rail_height = 5
)

workspace = cq.Workplane('XY')
workspace.add(f)

cq.exporters.export(workspace,'out/stairs.stl')

if f.metadata:
    print(f.metadata)

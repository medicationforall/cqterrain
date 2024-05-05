import cadquery as cq # Main cadquery library.
from cqterrain import stairs #Import stair generator code.

# Make an instance of the stairs shape with the following parameters.
ex = stairs(
    length = 30,
    width = 10,
    height = 30,
    run = 5,
    stair_length_offset = 0,
    stair_height = 1,
    stair_height_offset = 0,
    rail_width = 1,
    rail_height = 5
)

# Add the stairs to a workplane.
workspace = cq.Workplane('XY')
workspace.add(ex)

# Write to stl file.
cq.exporters.export(workspace,'stl/stairs.stl')


import cadquery as cq
from  cqterrain  import room

ex = room.make_room(
    length=104,
    width=79,
    height=40,
    wall_width=4,
    floor_height=3,
    floor_padding=2
)

# Add the stairs to a workplane.
workspace = cq.Workplane('XY')
workspace.add(ex)

# Write to stl file.
cq.exporters.export(workspace,'out/room.stl')

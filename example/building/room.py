import cadquery as cq
from  cqterrain.building  import Room

ex = Room(
    length=104,
    width=79,
    height=40,
    wall_width=4,
    floor_height=3,
    floor_padding=2
)

ex.make()
part = ex.build()

# Add the stairs to a workplane.
workspace = cq.Workplane('XY')
workspace.add(part)

# Write to stl file.
cq.exporters.export(workspace,'stl/room.stl')

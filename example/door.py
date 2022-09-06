import cadquery as cq
from  cqterrain  import Door

ex = Door()

ex.make()
part = ex.build()

# Add the stairs to a workplane.
workspace = cq.Workplane('XY')
workspace.add(part)

# Write to stl file.
cq.exporters.export(workspace,'out/door.stl')

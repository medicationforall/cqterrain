import cadquery as cq
from cqterrain.door import BlastDoor

bp = BlastDoor()

bp.length = 25
bp.width = 5
bp.height = 32
bp.fillet = 3
bp.chamfer = .6

bp.bar_height = 3
bp.bar_width = 1
bp.bar_margin_z = 5
bp.bar_margin_x = 1.5
bp.bar_cap_length = 3

bp.handle_height = 1.5
bp.handle_radius = 4
bp.handle_rotation = -15

bp.make()
blast_door = bp.build()
#show_object(blast_door)
cq.exporters.export(blast_door,'stl/door_blastDoor.stl')

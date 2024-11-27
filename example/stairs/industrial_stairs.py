import cadquery as cq
from cqspoolterrain import Stairs

bp = Stairs()
bp.length = 75
bp.width = 75
bp.height = 50
bp.stair_count = 5
bp.stair_chamfer = .5
bp.render_step_cut = True
bp.render_hollow = True
bp.cut_padding = 10
bp.make()
ex_stairs = bp.build()

#show_object(ex_stairs)
cq.exporters.export(ex_stairs,"stl/stairst_industrial_stairs.stl")
import cadquery as cq
from cqterrain.swivel import Swivel

bp = Swivel()
bp.channel_width = .8
bp.plate_x_translate = 40

bp.make()
ex_base = bp.build()

#show_object(ex_base)
cq.exporters.export(ex_base,"stl/swivel.stl")
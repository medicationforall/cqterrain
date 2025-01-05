import cadquery as cq
from cqterrain.shieldwall import BaseCut

bp_base_cut = BaseCut()
bp_base_cut.length = 75
bp_base_cut.width = 10
bp_base_cut.height = 4
bp_base_cut.angle = 30

bp_base_cut.make()

result = bp_base_cut.build()

#show_object(result)
cq.exporters.export(result, 'stl/shieldwall_base_cut.stl')
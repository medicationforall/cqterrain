import cadquery as cq
from cqterrain.bridge import BaseRamp

bp_ramp = BaseRamp()
bp_ramp.length = 75*2
bp_ramp.width = 75*2
bp_ramp.height = 50
bp_ramp.make()

ex_ramp = bp_ramp.build()

#show_object(ex_ramp)
cq.exporters.export(ex_ramp,'stl/bridge_ramp.stl')
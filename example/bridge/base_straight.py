import cadquery as cq
from cqterrain.bridge import BaseStraight

bp_ramp = BaseStraight()

length:float = 75*2
width:float = 75*2
height:float = 50
bp_ramp.make()

ex_straight = bp_ramp.build()

#show_object(ex_ramp)
cq.exporters.export(ex_straight,'stl/bridge_straight.stl')
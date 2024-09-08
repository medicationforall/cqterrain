import cadquery as cq
from cqterrain.bridge import BaseStraight

bp_straight = BaseStraight()

bp_straight.length = 75*2
bp_straight.width = 75*2
bp_straight.height = 50
bp_straight.make()

ex_straight = bp_straight.build()

#show_object(ex_straight)
cq.exporters.export(ex_straight,'stl/bridge_straight.stl')
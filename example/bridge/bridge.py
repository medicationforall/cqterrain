import cadquery as cq
from cqterrain.bridge import Bridge

bp_bridge = Bridge()

bp_bridge.straight_count = 1
bp_bridge.width = 75*2
bp_bridge.height = 50

bp_bridge.make()
ex_bridge = bp_bridge.build()

#show_object(ex_bridge)
cq.exporters.export(ex_bridge,'stl/bridge.stl')
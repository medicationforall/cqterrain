import cadquery as cq
from cqterrain.shieldwall import CapGreeble

bp_cap = CapGreeble()

bp_cap.length = 20
bp_cap.width = 8
bp_cap.height = 30
bp_cap.top_fillet = 2.9
bp_cap.side_fillet = 2.5
bp_cap.operation = 'chamfer'

bp_cap.render_grill = True
bp_cap.grill_height = 2
bp_cap.grill_padding_top = 1
bp_cap.grill_padding_left = 2
bp_cap.grill_margin = .5

bp_cap.make()

result = bp_cap.build()

#show_object(result)
cq.exporters.export(result, 'stl/shieldwall_cap_greeble.stl')
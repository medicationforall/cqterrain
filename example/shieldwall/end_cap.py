import cadquery as cq
from cqterrain.shieldwall import EndCap

cap_bp =  EndCap()
cap_bp.length = 15
cap_bp.width = 20
cap_bp.height = 25
cap_bp.base_height = 5.6
cap_bp.side_margin = -2
cap_bp.side_height = 1
cap_bp.top_height = 2

cap_bp.cut_width = 3
cap_bp.middle_width_inset = -6

cap_bp.render_greeble = True
cap_bp.greeble_padding_y = 1

cap_bp.render_magnets = True
cap_bp.magnet_padding = 1
cap_bp.magnet_padding_x = 2


cap_bp.make()
cap_ex = cap_bp.build()
cap_ex_assembly = cap_bp.build_assembly()

#show_object(cap_ex)
cq.exporters.export(cap_ex, 'stl/shieldwall_end_cap.stl')
cap_ex_assembly.save("gltf/shieldwall_end_cap.gltf")


import cadquery as cq
from cqterrain.shieldwall import ArchSet

arch_set_bp = ArchSet()
arch_set_bp.height=25
arch_set_bp.straight_count = 4
arch_set_bp.straight_bp.mesh_width = 6

arch_set_bp.end_bp.render_greeble = False
arch_set_bp.corner_bp.render_greeble = False
arch_set_bp.make()
arch_set = arch_set_bp.build()

#show_object(arch_set.translate((0,0,25)))
#show_object(arch_set_bp.straight_bp.key_template.translate((-75,0,1)))

#cq.exporters.export(arch_set, 'stl/shieldwall_arch_set.stl')
#if arch_set_bp.straight_bp.key_template:
cq.exporters.export(arch_set.translate((0,0,12.5)).add(arch_set_bp.straight_bp.key_template.translate((-75,0,1))),'stl/shieldwall_arch_set.stl')
#else:
#    raise Exception('Could not resolve example key template')

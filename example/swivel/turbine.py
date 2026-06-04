import cadquery as cq
from cqterrain.swivel import Turbine

bp = Turbine()

bp.mast_height = 35
bp.mast_diameter = 5

bp.cap_diameter = 6
bp.cap_height = 4

bp.blade_count = 3
bp.blade_length = 10
bp.blade_width = 3
bp.blade_rotate = (90+45)
bp.blade_radius = 12
bp.blade_offset = 0

bp.fin_count = 6

bp.make()
ex_top = bp.build()

#show_object(ex_top)
cq.exporters.export(ex_top,"stl/swivel_turbine.stl")
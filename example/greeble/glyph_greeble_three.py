import cadquery as cq
from cqterrain.greeble import CircuitGlyph 
from cadqueryhelper.shape import ring

bp_glyph = CircuitGlyph()
bp_glyph.debug= True
bp_glyph.line_width = 1
bp_glyph.point_diameter = 3
bp_glyph.line_height = 1
bp_glyph.kind = 'arc'

bp_glyph.render_outline = False
bp_glyph.outline_margin = 0

bp_glyph.add_point(0,0,ring(4,2,3))
bp_glyph.add_point_rotate(10,0,20,cq.Workplane("XY").cylinder(3,1.5))
bp_glyph.add_point_rotate(15,0,40,cq.Workplane("XY").cylinder(3,1.5))
bp_glyph.add_point_rotate(0,-10,0,cq.Workplane("XY").cylinder(3,1.5))
bp_glyph.make()

ex_glyph = bp_glyph.build()

#show_object(ex_glyph)
cq.exporters.export(ex_glyph,'stl/greeble_circuit_glyph_three.stl')
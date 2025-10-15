import cadquery as cq
from cqterrain.greeble import CircuitGlyph 
from cadqueryhelper.shape import ring

bp_glyph = CircuitGlyph()

bp_glyph.add_point(0,6,ring(4,2,3))
bp_glyph.add_point(6,-1)
bp_glyph.add_point(-9,-6,cq.Workplane("XY").cylinder(3,1.5))
bp_glyph.add_point(-15,-0)
bp_glyph.add_point(-5,-0,ring(6,4,3))
bp_glyph.add_point(-8,9,cq.Workplane("XY").box(3,3,2).translate((0,0,0.5)))
bp_glyph.make()

ex_glyph = bp_glyph.build()

#show_object(ex_glyph)
cq.exporters.export(ex_glyph,'stl/greeble_circuit_glyph_one.stl')
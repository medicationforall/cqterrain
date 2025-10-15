import cadquery as cq
from cqterrain.greeble import CircuitGlyph 
from cadqueryhelper.shape import ring

#----------------
spoke = cq.Workplane("XY").box(4,1,2).translate((5.5,0,0))
spoke_two =spoke.rotate((0,0,1),(0,0,0),-90) 
spoke_three =spoke.rotate((0,0,1),(0,0,0),-180)

large = (
    ring(8,6,2)
    .add(spoke)
    .add(spoke_two)
    .add(spoke_three)
).translate((0,0,.5))
#----------------

bp_glyph = CircuitGlyph()
bp_glyph.line_width = 1.5
bp_glyph.add_point(0,0, ring(4,2,2).translate((0,0,.5)))
bp_glyph.add_point(0,10,large)
bp_glyph.make()

ex_glyph = bp_glyph.build()
#show_object(ex_glyph.translate((0,0,0)))

cq.exporters.export(ex_glyph,'stl/greeble_circuit_glyph_two.stl')
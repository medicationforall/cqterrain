import cadquery as cq
from cqterrain.spool import SpoolLogoStack

bp_spool_stack = SpoolLogoStack()
bp_spool_stack.font_size = 55
bp_spool_stack.font_width = 55
bp_spool_stack.font_center_offset = -10
bp_spool_stack.logo_text = "MINI FOR ALL"
bp_spool_stack.word_offset = [0,3,4]
bp_spool_stack.render_spool = True
bp_spool_stack.make()
spool_logo_ex = bp_spool_stack.build()

#show_object(spool_logo_ex)
cq.exporters.export(spool_logo_ex,"stl/spool_logo_2.stl")
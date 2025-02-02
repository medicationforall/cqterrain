import cadquery as cq
from cqterrain.book import Bookcase

bp_case = Bookcase()
bp_case.length = 100
bp_case.width = 15
bp_case.segments = 4
bp_case.minus_width = 3
bp_case.seed = "purple"
bp_case.book_count =(16,30,1)
bp_case.min_book_height = 6

#closed
bp_case.bottom_align = True
bp_case.page_width_inset=0.5
bp_case.back_translate = 1

# open
#bp_case.bottom_align = False#True
#bp_case.page_width_inset=1#0.5
#bp_case.back_translate = 0#1

bp_case.render_books = True
bp_case.make()

ex_case = bp_case.build()
#show_object(ex_case)

cq.exporters.export(ex_case,'stl/book_bookcase_books.stl')
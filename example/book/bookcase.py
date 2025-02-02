import cadquery as cq
from cqterrain.book import bookcase 

ex_bookcase = bookcase(
    length = 75,
    width = 20,
    height = 60,
    segments = 4,
    margin_top = 1.5,
    margin_sides = 2,
    back_translate = 1
)
#show_object(ex_bookcase)
cq.exporters.export(ex_bookcase,'stl/book_bookcase.stl')
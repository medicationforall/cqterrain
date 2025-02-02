import cadquery as cq
from cqterrain.book import book

ex_book = book(
    length = 3, 
    width = 10, 
    height = 12,
    binder_width = 0.5,
    page_width = 9,
    page_height = 11,
    bottom_align = False,
    fillet = 0.5
)

#show_object(ex_book)
cq.exporters.export(ex_book,'stl/book.stl')
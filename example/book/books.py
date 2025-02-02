import cadquery as cq
from cqterrain.book import books

seed = "pink"
ex_books,dim = books(
    count = 5,
    length = (2.0,4.0,0.5),
    width = (8,11,0.5), 
    height = (8,12,0.5),
    binder_width = .5,
    page_width_inset = 1,
    page_height_inset = 1,
    bottom_align = True,
    seed=seed
)

#show_object(ex_books)
cq.exporters.export(ex_books,f'stl/book_books_{seed}.stl')

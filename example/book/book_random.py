import cadquery as cq
from cqterrain.book import book_random

seed = 'test'

ex_book, dim = book_random(
    length=(2.0,8.0,0.5),
    width = (8,11,0.5), 
    height = (8,12,0.5),
    binder_width=.5,
    page_width_inset = 1,
    page_height_inset=1,
    bottom_align = False,
    seed=seed
)

#show_object(ex_book)
cq.exporters.export(ex_book,f'stl/book_random_{seed}.stl')


seed = 'blue'
blue_book, dim = book_random(
    length=(2.0,8.0,0.5),
    width = (8,11,0.5), 
    height = (8,12,0.5),
    binder_width=.5,
    page_width_inset = 1,
    page_height_inset=1,
    bottom_align = False,
    seed=seed
)

#show_object(blue_book)
cq.exporters.export(blue_book,f'stl/book_random_{seed}.stl')



seed = 'green'
green_book, dim = book_random(
    length=(2.0,8.0,0.5),
    width = (8,11,0.5), 
    height = (8,12,0.5),
    binder_width=.5,
    page_width_inset = 1,
    page_height_inset=1,
    bottom_align = False,
    seed=seed
)

#show_object(green_book)
cq.exporters.export(green_book,f'stl/book_random_{seed}.stl')

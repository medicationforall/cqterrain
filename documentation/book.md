# Book

---

## Book
Method for making a solid that resembles a blosed book.

### parameters
* length: float 
* width: float 
* height: float
* binder_width: float
* page_width: float
* page_height: float
* bottom_align: bool
* fillet: float

``` python
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

show_object(ex_book)
```

![](image/book/01.png)

* [source](../src/cqterrain/book.py)
* [example](../example/book/book.py)
* [stl](../stl/book.stl)

---

## Book Random
Randomized book generator. Wrapper function around [book](#book) that adds min and max values to parameters.

### parameters
* length: tuple[float,float,float]|float
* width: tuple[float,float,float]|float 
* height: tuple[float,float,float]|float
* binder_width: tuple[float,float,float]|float
* page_width_inset: float
* page_height_inset: float
* bottom_align: bool
* fillet: float
* seed: str|None

### returns
Returns a cadquery workplane and a tuple which has length, width and height of the generated book.

``` python
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

show_object(ex_book)
```

![](image/book/02.png)

* [source](../src/cqterrain/book.py)
* [example](../example/book/book_random.py)
* [stl](../stl/book_random_test.stl)

### Alternative seed blue
``` python
import cadquery as cq
from cqterrain.book import book_random

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

show_object(blue_book)
```

![](image/book/03.png)

* [source](../src/cqterrain/book.py)
* [example](../example/book/book_random.py)
* [stl](../stl/book_random_blue.stl)

### Alternative seed green
``` python
import cadquery as cq
from cqterrain.book import book_random

seed = 'green'

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

show_object(green_book)
```

![](image/book/04.png)

* [source](../src/cqterrain/book.py)
* [example](../example/book/book_random.py)
* [stl](../stl/book_random_green.stl)

---

## Books

### parameters
* count: tuple[int,int,int]|int
* length: tuple[float,float,float]|float
* width: tuple[float,float,float]|float
* height: tuple[float,float,float]|float
* binder_width: tuple[float,float,float]|float
* page_width_inset: float
* page_height_inset: float
* bottom_align: bool
* seed: str

``` python
import cadquery as cq
from cqterrain.book import books

seed = "pink"
ex_books = books(
    count=5,
    length = (2.0,4.0,0.5),
    width = (8,11,0.5), 
    height = (8,12,0.5),
    binder_width = .5,
    page_width_inset = 1,
    page_height_inset = 1,
    bottom_align = True,
    seed=seed
)

show_object(ex_books)
```

![](image/book/05.png)

* [source](../src/cqterrain/books.py)
* [example](../example/book/books.py)
* [stl](../stl/books_pink.stl)

---
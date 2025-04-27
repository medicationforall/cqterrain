import cadquery as cq
from cadqueryhelper import Base
from . import bookcase, books

class Bookcase(Base):
    def __init__(self):
        super().__init__()
        # parameters
        self.length:float = 75
        self.width:float = 20
        self.height:float = 60
        self.segments:int = 4
        self.margin_top:float = 1.5
        self.margin_sides:float = 2
        self.back_translate:float = 0
        
        self.render_books:bool = True
        self.book_length:float|tuple[float,float,float] = (2.0,4.0,0.5)
        self.minus_width:float = 5
        self.seed:str = "orange"
        self.book_count:int|tuple[int,int,int] = 24
        self.bottom_align:bool = False
        self.binder_width:float = .5
        self.page_width_inset:float = 1
        self.page_height_inset:float = 1
        self.min_book_height:float = 8
        
        # shapes
        self.case = None
        self.books = None
        
    def calculate_segment_spacing(self):
        spacing = ((self.height-self.margin_top*2)/self.segments)
        return spacing
        
    def calulate_segment_height(self):
        spacing = ((self.height-self.margin_top*2)/self.segments)
        segment_height = spacing - self.margin_top * 2
        return segment_height
        
    def make_bookcase(self):
        self.case = bookcase(
            length = self.length,
            width = self.width,
            height = self.height,
            segments = self.segments,
            margin_top = self.margin_top,
            margin_sides = self.margin_sides,
            back_translate = self.back_translate
        )
        
    def make_books(self):
        # = cq.Workplane("XY").box(10,10,10)
    
        def book_generator():
            count = 0
            def add_books(loc:cq.Location)->cq.Shape:
                nonlocal count
                count+=1
                segment_height = self.calulate_segment_height()
                add_seed = f'{self.seed}_{count}'
                ex_books,dim = books(
                    count=self.book_count,
                    length = self.book_length,
                    width = (self.width-self.minus_width,self.width,0.5), 
                    height = (self.min_book_height,segment_height,0.5),
                    binder_width = self.binder_width,
                    page_width_inset = self.page_width_inset,
                    page_height_inset = self.page_height_inset,
                    bottom_align = self.bottom_align,
                    seed=add_seed
                )
                
                ex_books = (
                    ex_books
                    .rotate((0,0,1),(0,0,0),180)
                    .translate((dim[0]/2,-dim[1]/2,-segment_height/2))
                    .rotate((1,0,0),(0,0,0),90)
                )
                
                return ex_books.val().located(loc) #type:ignore
            return add_books
        
        adder_method = book_generator()
        spacing = self.calculate_segment_spacing()
        group_books = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = self.length, 
                ySpacing = spacing,
                xCount = 1, 
                yCount= self.segments, 
                center = True)
            .eachpoint(adder_method)
        ).rotate((1,0,0),(0,0,0),-90)
        
        self.books = group_books
        
        
    def make(self, parent=None):
        super().make(parent)
        self.make_bookcase()
        
        if self.render_books:
            self.make_books()
        
    def build(self):
        super().build()
        
        scene = cq.Workplane("XY")
        
        if self.case:
            scene = scene.add(self.case)
            
        if self.render_books and self.books:
            scene = scene.union(self.books)
        return scene
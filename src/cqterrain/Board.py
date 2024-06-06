import cadquery as cq
from cadqueryhelper import Base

def square(
        length:float = 25, 
        width:float = 25,
        height:float = 12, 
        shell:float = 3
    ):
    sq = cq.Workplane("XY").box(length,width,height)
    return sq.faces("-Z").shell(-shell)

class Board(Base):
    def __init__(self):
        super().__init__()
        #properties
        self.length:float = 25*10
        self.width:float = 25*10
        self.height:float = 12.5
        
        self.x_count:int = 8
        self.y_count:int = 8
        self.shell:float = 1.5
        self.height_offset:float = 2.5
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.squares:cq.Workplane|None = None

    def __make_outline(self):
        self.outline = (
            cq.Workplane("XY")
            .box(
                self.length, 
                self.width, 
                self.height
            )
        )
        
    def __make_squares(self):
        sq_length = self.length/self.x_count
        sq_width = self.width/self.y_count
        count = 0
        row = 0
        
        def add_square(loc:cq.Location) -> cq.Shape:
            nonlocal count
            nonlocal row
            height = self.height
            lowered = False
            
            if count % self.x_count == 0:
                row+=1
                #log(f'increased row count {row=}')
            
            #well that was painful mistake
            if count%2==0 and row%2==0 or count%2==1 and row%2==1:
                #log(f'found cell to lower {count=}, {row=}')
                height = self.height - self.height_offset
                lowered=True
                
            sq = square(sq_length, sq_width, height, self.shell)
            
            if lowered:
                sq = sq.translate((0,0,-(self.height_offset/2)))
                
            count+=1
            return sq.val().located(loc) #type: ignore
        
        squares = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = sq_length, 
                ySpacing = sq_width,
                xCount = self.x_count, 
                yCount= self.y_count, 
                center = True)
            .eachpoint(callback = add_square)
        )
        self.squares = squares
        
        
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_outline()
        self.__make_squares()
        
    def build(self) -> cq.Workplane:
        super().build()
        scene = (
            cq.Workplane("XY")
            #.union(self.outline)
            .union(self.squares)
        )
        return scene
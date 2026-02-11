import cadquery as cq
from cadqueryhelper import Base
from cadqueryhelper.grid import (
    grid_points_mod, cell_stretch_points,
    grid_cell_random, join_cells_interlock,
    points_randomize
)

class ModPattern(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 60
        self.width:float = 25
        self.height:tuple[float,float,float]|float = 2
        self.render_points:bool = False
        self.debug:bool = False
        
        #points
        self.x_spacing:list[float] = [5,10]
        self.y_spacing:list[float] = [5,10]
        self.row_x_mod:list[int] = [0,1]
        self.row_x_offset:list[float] = [0,-2.5]
        
        #randomize
        self.randomize_points:bool = False
        self.shift_x:tuple[float,float,float] = (-2,2,.5)
        self.shift_y:tuple[float,float,float] = (-2,2,.5)
        self.seed:str = 'test'
        
        #cells
        self.x_stretch:int = 1
        self.y_stretch:int = 1
        
        #grid
        self.taper:tuple[float,float,float]|float|None = 25
        self.offset:tuple[float,float,float]|float|None = 0
        self.grid_offset_x:float = 0
        self.grid_offset_y:float = 0
        
        self.column_pad:int = 0
        self.row_pad:int = 0
        
        #interlock
        self.interlock_cells:bool = False
        self.start:int = 1
        self.top_end_index:int = 3
        self.bottom_start_index:int = 2
        self.top_cap_index:int = 3
        
        #points
        self.points = None
        self.stream = None
        self.cell_points = None
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.grid:cq.Workplane|None = None

        
    def calculate_columns(self):
        index = 1
        columns = 1
        length = 0
        
        while length < self.length:
            columns+=1
            
            l = self.x_spacing[index % len(self.x_spacing)]
            length += l
            
            index += 1
            
        return columns + self.column_pad
    
    def calculate_rows(self):
        index = 1
        rows = 1
        width = 0
        
        while width < self.width:
            rows+=1
            
            l = self.y_spacing[index % len(self.y_spacing)]
            width += l
            
            index += 1
            #log(f'width {width}, index {index}')
            
        return rows + self.row_pad
        
    def make_outline(self):

        if type(self.height) is tuple:
            height = self.height[1]
        else:
            height:float = self.height

        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            height
        )
        
        self.outline = outline
        
    def make_points(self):
        columns = self.calculate_columns()
        rows = self.calculate_rows()
        
        points, stream = grid_points_mod(
            columns = columns,
            rows = rows,
            x_spacing = self.x_spacing,
            y_spacing = self.y_spacing,
            row_x_mod = self.row_x_mod,
            row_x_offset =  self.row_x_offset
        )
        
        self.points = points
        self.stream = stream
        
    def make_randomize_points(self):
        r_points,r_stream = points_randomize(
            self.points,
            shift_x = self.shift_x,
            shift_y = self.shift_y,
            seed = self.seed
        )
        self.points = r_points
        self.stream = r_stream
        
    def make_cell_points(self):
        cell_points = cell_stretch_points(
            self.points,
            x_stretch = self.x_stretch,
            y_stretch = self.y_stretch
        )
        
        self.cell_points = cell_points
        
    def make_interlock_cells(self):
        joined_cells = join_cells_interlock(
            self.points,
            self.cell_points,
            start = self.start,
            top_end_index = self.top_end_index,
            bottom_start_index = self.bottom_start_index,
            top_cap_index = self.top_cap_index
        )
        
        self.cell_points = joined_cells
        
    def make_grid(self):
        grid = grid_cell_random(
            self.cell_points,
            height = self.height,
            taper = self.taper,
            offset = self.offset,
            seed = self.seed
        )
        
        self.grid = grid
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_points()
        if self.randomize_points:
            self.make_randomize_points()
            
        self.make_cell_points()
        
        if self.interlock_cells:
            self.make_interlock_cells()
        self.make_grid()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            if type(self.height) is tuple:
                height = self.height[1]
            else:
                height:float = self.height
            part = part.add(self.outline.translate((0,0,height/2)))
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.render_points and self.stream:
            part = (
                part.pushPoints(self.stream)
                .box(1,1,1)
                .translate((-self.length/2,self.width/2,0))
            )
        
        if self.grid:
            part = part.union(
                self.grid
                .translate((-self.length/2,self.width/2,0))
                .translate((self.grid_offset_x,self.grid_offset_y,0))
            )

            if type(self.height) is tuple:
                height = self.height[1]
            else:
                height:float = self.height
            
            if self.debug:
                part = part.add(self.outline.translate((0,0,height/2)))
            else:
                part = part.intersect(self.outline.translate((0,0,height/2)))
        
        return part
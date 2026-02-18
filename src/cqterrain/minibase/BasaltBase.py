import cadquery as cq
from .PointGridBase import PointGridBase
from ..floor import ModPattern

class BasaltBase(PointGridBase):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 30
        self.width:float = 25
        self.height:float = 3
        self.seed:str = 'test'

        #blueprints
        self.bp_grid:ModPattern = ModPattern()
        self.bp_grid.interlock_cells = True
        self.bp_grid.randomize_points = True
        self.bp_grid.x_spacing = [5,10]
        self.bp_grid.y_spacing = [5]
        self.bp_grid.row_x_offset = [0,-2.25]
        self.bp_grid.height = (0,2,.25)
        self.bp_grid.taper = (-5,25,5)
        self.bp_grid.offset = (-.75,0,.25)
        
        self.bp_grid.shift_x = (-1,1,.5)
        self.bp_grid.shift_y = (-1,1,.5)
        self.bp_grid.column_pad = 2
        self.bp_grid.row_pad = 2
        self.bp_grid.grid_offset_x = -10
        self.bp_grid.grid_offset_y = 5
        
        #shapes
        self.outline:cq.Workplane|None = None

    def make_grid(self):
        length = self.length
        width = self.width
        
        if self.base_type == 'circle' or self.base_type == 'hexagon':
            length = self.diameter
            width = self.diameter
        elif self.base_type == 'ellipse':
            length = self.diameter
            width = self.diameter_y
        
        self.bp_grid.length = length
        self.bp_grid.width = width
        self.bp_grid.seed = self.seed
        self.bp_grid.make()
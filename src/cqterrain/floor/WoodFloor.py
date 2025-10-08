import cadquery as cq
from cadqueryhelper import Base
from  math import floor
import random


class WoodFloor(Base):
    
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 150
        self.width:float = 75
        self.height:float = 8
        
        #joist
        self.joist_width:float = 3
        self.joist_space:float = 12.5
        self.joist_count:float = 7
        self.render_joists:bool = False
        
        # Board
        self.board_width:float = 5
        self.board_width_spacer:float = .1
        self.board_height:float = 1.5
        
        #nail
        self.nail_diameter:float = .4
        self.nail_overlap_height:float = .2
        self.nail_x_margin:float = .5
        self.nail_y_margin:float = .5
        
        # grid
        self.seed:str = "redd2"
        self.board_lenghs:list[int] = [1,4]
        self.board_break_width:float = .2
        self.grid:list[str] = []
        
        #shapes
        self.outline:cq.Workplane|None = None
        
        self.joist:cq.Workplane|None = None
        self.joists:cq.Workplane|None = None
        
        self.board:cq.Workplane|None = None
        self.boards:cq.Workplane|None = None
        
        self.nail:cq.Workplane|None = None
        self.nail_pair:cq.Workplane|None = None
        self.nail_quad:cq.Workplane|None = None
        
        self.board_break:cq.Workplane|None = None
        self.board_breaks:cq.Workplane|None = None
        
        
    def make_outline(self):
        self.outline = cq.Workplane("XY").box(
            self.length, 
            self.width, 
            self.height
        )
        
        
    def make_joist(self):
        self.joist = cq.Workplane("XY").box(
            self.length, 
            self.joist_width, 
            self.height-self.board_height
        )
        
        
    def calculate_joists_count(self):
        return floor(self.width / self.joist_space)+1
    
    
    def calculate_boards_count(self):
        return floor(self.length / self.board_width)
    
    
    def add_joist(self, loc:cq.Location) -> cq.Shape:
        return self.joist.val().located(loc) #type:ignore
        
    
    def make_joists(self):
        y_count = self.calculate_joists_count()
        #log(f"test {y_count=}")
        #joists = cq.Workplane("XY")
        
        joists = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = 0, 
                ySpacing = self.joist_space,
                xCount = 1, 
                yCount= y_count, 
                center = True)
            .eachpoint(self.add_joist)
        )
        
        self.joists = joists
        
        
    def make_board(self):
        self.board = cq.Workplane("XY").box(
            self.board_width - self.board_width_spacer*2, 
            self.width, 
            self.board_height
        )
        
        
    def add_board(self, loc:cq.Location) -> cq.Shape:
        return self.board.val().located(loc) #type:ignore
        
    
    def make_boards(self):
        x_count = self.calculate_boards_count()
        
        boards = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = self.board_width, 
                ySpacing = 0,
                xCount = x_count, 
                yCount= 1, 
                center = True)
            .eachpoint(self.add_board)
        )
        
        self.boards = boards
        
        
    def make_nail(self):
        height = self.board_height + self.nail_overlap_height
        nail = cq.Workplane("XY").cylinder(height, self.nail_diameter/2)
        
        self.nail = nail.translate((0,0,self.nail_overlap_height/2))
        
        
    def make_nail_pair(self):
        if self.nail:
            translate_x = self.board_width/2-self.nail_diameter/2-self.nail_x_margin
            nail_one = self.nail.translate((translate_x,0,0))
            nail_two  = self.nail.translate((-translate_x,0,0))
            
            self.nail_pair = nail_one.union(nail_two)
        else:
            raise Exception("Could not resolve self.nail")
        
        
    def make_nail_quad(self):
        if self.nail_pair:
            translate_y = self.joist_width/2-self.nail_diameter/2-self.nail_y_margin
            nails_one = self.nail_pair.translate((0,translate_y,0))
            nails_two = self.nail_pair.translate((0,-translate_y,0))
            self.nail_quad = nails_one.union(nails_two)
        else:
            raise Exception("Could not resolve self.nail")
        
    
    def make_nails(self):
        
        y_count = self.calculate_joists_count()
        x_count = self.calculate_boards_count()
        #log(f"test {y_count=}")
        #joists = cq.Workplane("XY")
        
        nail_grid = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = self.board_width, 
                ySpacing = self.joist_space,
                xCount = x_count, 
                yCount= y_count, 
                center = True)
            .eachpoint(self.add_nail_grid(self.grid, y_count))
        )
        
        self.nails = nail_grid
        
        
    def make_grid(self):
        y_count = self.calculate_joists_count()
        x_count = self.calculate_boards_count()
        
        #log(f' make grid {y_count=} {x_count=}')
        break_point = random.choice(self.board_lenghs)
        grid = []
        
        #log(f"{break_point=}")
        
        for x in range(x_count):
            row = []
            for y in range(y_count):
                last_cell = (y == y_count-1)
                #log(f"{last_cell=} {y=} {y_count-1}")
                adjacent_cell = "f"
                
                if len(grid) > 0:
                    adjacent_cell = grid[x-1][y]
                    
                if adjacent_cell == "b" and  break_point == 0:
                    #log("found joining lines")
                    break_point += 1
                    
                if break_point == 0:
                    #log('found break point')
                    if last_cell or y == 0:
                        row.append("f")
                    else:
                        row.append("b")
                        break_point=random.choice(self.board_lenghs)
                else:
                    break_point -=1
                    row.append("f")
                    
            grid.append(row)
            
        #log(f'this is a grid {grid}')
        self.grid = grid
        
        
    def make_board_break(self):
        board_break = cq.Workplane("XY").box(self.board_width, self.board_break_width,self.board_height)
        self.board_break = board_break
        
    def add_nail_grid(self, grid, y_count:int):
        count = 0
        x_index = -1
        
        def add_nail_quad(loc:cq.Location) -> cq.Shape:
            nonlocal count
            nonlocal x_index
            nonlocal grid
            nonlocal y_count
            end = False
            
            y_index = count % y_count
            if y_index == 0:
                x_index+=1
                end = True
                
            if y_index == y_count-1:
                end = True
            
            result = grid[x_index][y_index]
            
            
            count+=1
            
            #log(f"nail cell {count=} {x_index=} {y_index=} {result=}")
            
            if end:
                #log("I think this is an end cap")
                return self.nail_quad.val().located(loc) #type:ignore
            
            if result=="b":
                return self.nail_quad.val().located(loc) #type:ignore
            else:
                return self.nail_pair.val().located(loc) #type:ignore
        
        return add_nail_quad
        
        
    def add_board_break(self, grid, y_count:int):
        count = 0
        x_index = -1
        def fill_cell(loc:cq.Location)->cq.Shape:
            nonlocal count
            nonlocal x_index
            nonlocal grid
            nonlocal y_count
            
            y_index = count % y_count
            if y_index == 0:
                x_index+=1
            
            result = grid[x_index][y_index]
            
            count+=1
            
            #log(f"cell {count=} {x_index=} {y_index=} {result=}")
            cell = cq.Workplane("XY")
            
            if result=="b":
                cell = cell.union(self.board_break)
                cell = cell.val().located(loc) #type:ignore
                self.board_breaks = self.board_breaks.add(cell) #type:ignore
                return cell #type:ignore
            else:
                cell= cq.Workplane("XY").box(1,1,1)
                return cell.val().located(loc) #type:ignore
        return fill_cell
        
    
    def make_board_breaks(self):
        self.board_breaks = cq.Workplane("XY")
        
        y_count = self.calculate_joists_count()
        x_count = self.calculate_boards_count()
        
        temp_board_breaks = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = self.board_width, 
                ySpacing = self.joist_space,
                xCount = x_count, 
                yCount= y_count, 
                center = True)
            .eachpoint(self.add_board_break(self.grid, y_count))
        )
        
        #self.board_breaks = board_breaks
        
    def make(self):
        super().make()
        if(self.seed):
            random.seed(self.seed)
            
        self.make_outline()
        
        self.make_joist()
        self.make_joists()

        self.make_board()
        self.make_boards()
        
        self.make_grid()
        
        self.make_board_break()
        self.make_board_breaks()
        
        self.make_nail()
        self.make_nail_pair()
        self.make_nail_quad()
        self.make_nails()

    def build_floor(self)->cq.Workplane:
        part = cq.Workplane("XY")

        if self.outline and  self.nails: 
            nails = self.outline.intersect(self.nails)

        if self.boards and self.board_breaks:
            boards = self.boards.cut(self.board_breaks)

        part = part.add(boards)
        part = part.add(nails)
        return part

    def build_joists(self)->cq.Workplane:
        part = cq.Workplane("XY")

        if self.outline and self.joists:
            joists = self.outline.intersect(self.joists)
        part = part.add(joists)
        return part
        
    def build(self):
        super().build()
        part = cq.Workplane("XY")
        floor = self.build_floor()
        
        if self.render_joists:
            joists = self.build_joists()
            part = part.add(joists)
            part = part.add(floor.translate((0,0,self.height/2)))
        else:
           part = part.add(floor) 
        return part
    
    def build_assembly(self):
        joists = self.outline.intersect(self.joists)
        
        nails = self.outline.intersect(self.nails)
        nails = nails.translate((0,0,self.height/2))
        
        boards = self.boards.cut(self.board_breaks)
        boards = boards.translate((0,0,self.height/2))
        
        assembly = cq.Assembly()
        assembly.add(joists, color=cq.Color(0,0,1), name="joists")
        assembly.add(nails, color=cq.Color(0,1,0), name="nails")
        assembly.add(boards, color=cq.Color(1,0,0), name="boards")
        return assembly
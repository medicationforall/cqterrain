import cadquery as cq
from cadqueryhelper import Base
import math
from cadqueryhelper.shape import ring

class RoundBrickFloor(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.diameter:float = 100
        self.height:float = 4
        self.rows:int = 10
        self.block_count:int = 8
        
        self.ring_spacing:float = 1.5
        self.spacer_width:float = 1
        
        self.ring_skip_index:int|None = None

        #shapes
        self.outline:cq.Workplane|None = None
        self.odd_rings:cq.Workplane|None = None
        self.even_rings:cq.Workplane|None = None
        self.spacer:cq.Workplane|None = None
        
        
    def calculate_ring_size(self)->float:
        size = self.diameter / self.rows
        return size
    
    def calculate_circumference(self, radius:float)->float:
        circumference = 2 * math.pi * radius
        return circumference
    
    def make_spacer(self):
        spacer = (
            cq.Workplane("XY")
            .box(self.diameter/2, self.spacer_width,self.height)
            .translate((self.diameter/4,0,0))
        )
        spacers = cq.Workplane("XY")
        
        for i in range(self.block_count):
            rotate_degrees = 360 / self.block_count
            spacers = spacers.union(spacer.rotate((0,0,1),(0,0,0),rotate_degrees*i)) 
        self.spacer = spacers
    
    def make_rings(self):
        size = self.calculate_ring_size()
        odd_rings = cq.Workplane("XY")
        even_rings = cq.Workplane("XY")
        center = None
        
        for index in range(self.rows):
            if self.ring_skip_index and index < self.ring_skip_index:
                continue
            
            inner_diameter = size*index
            diameter = size * (index+1)
            
            if not inner_diameter:
                center = cq.Workplane("XY").cylinder(
                    self.height, 
                    diameter/2
                )
                
            else:
                #log(f"make ring {index} {inner_diameter=} {diameter=}")
                ring_row = ring(
                    diameter, 
                    inner_diameter+self.ring_spacing, 
                    self.height
                )
                
                if index % 2 ==1:
                    #log("even")
                    odd_rings = odd_rings.add(ring_row)
                else:
                    #log("odd")
                    even_rings = even_rings.add(ring_row) 

        self.even_rings = even_rings    

        if self.spacer:
            self.even_rings = self.even_rings.cut(self.spacer)
        
        if center:
            self.even_rings = self.even_rings.add(center)

        self.odd_rings = odd_rings

        if self.spacer:
            rotate_degrees = 360 / self.block_count
            self.odd_rings = self.odd_rings.cut(self.spacer).rotate((0,0,1),(0,0,0),rotate_degrees/2)
                
    def make_outline(self):
        outline = cq.Workplane("XY").cylinder(
            self.height, 
            self.diameter/2
        )
        self.outline = outline
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_spacer()
        self.make_rings()
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")

        if self.odd_rings:
            part = part.add(self.odd_rings)

        if self.even_rings:
            part = part.add(self.even_rings)
        
        return part
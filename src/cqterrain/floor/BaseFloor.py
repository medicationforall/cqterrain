import cadquery as cq
from cadqueryhelper import Base

class BaseFloor(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length = 30
        self.width = 25
        self.height = 60
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.floor:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline

    def make_floor(self):
        floor = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.floor = floor
        
    def make(self):
        super().make()
        self.make_floor()
        self.make_outline()
        
    def build_outline(self):
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part.add(self.outline)
        
        return part
        
    def build(self):
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.floor:
            part = part.add(self.floor)
        
        return part
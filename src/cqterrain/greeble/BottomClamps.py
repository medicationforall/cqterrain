import cadquery as cq
from cadqueryhelper import Base
from cadqueryhelper.shape import trapezoid

class BottomClamps(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 100
        self.width:float = 8
        self.height:float = 2
        
        self.clamp_height:float = 7
        self.clamp_chamfer:float = 1
        self.clamp_count:int = 3
        self.clamp_width:float = 8
        self.clamp_bottom_length:float = 25
        self.clamp_top_length:float = 10
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.base:cq.Workplane|None  = None
        self.clamps:cq.Workplane|None  = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_base(self):
        base = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.base = base
        
    def make_clamps(self):
        clamp  = trapezoid(
            length = self.clamp_width,
            width = self.clamp_bottom_length,
            height = self.clamp_height,
            top_width = self.clamp_top_length
        ).faces("|Y").chamfer(self.clamp_chamfer)
        
        clamp_segment_length = self.length / self.clamp_count
        clamps = cq.Workplane("XY")
        
        for i in range(self.clamp_count):
            clamps = clamps.add(clamp.translate((clamp_segment_length*i,0,0)))
            
        #panel_height = self.calculate_panel_height()
        z_translate = self.clamp_height/2
        x_translate = self.length/2+ -clamp_segment_length/2
        
        self.clamps = clamps.translate((-x_translate,0,z_translate))
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_base()
        self.make_clamps()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline.translate((0,0,self.height/2)))
            
        if self.clamps:
            part = part.union(self.clamps)
        
        return part
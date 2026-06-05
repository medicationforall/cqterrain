import cadquery as cq
from cadqueryhelper import Base
from cadqueryhelper.shape import trapezoid


class Panel(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 8
        self.width:float = 6
        self.height:float = 35
        self.outer_height:float = 15
        
        self.frame:float = 1.5
        self.frame_depth:float = 1
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.body:cq.Workplane|None = None
        self.frame_cut:cq.Workplane|None = None
        self.control_panel:cq.Workplane|None = None
        self.vents:cq.Workplane|None = None
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
    
    def make_body(self):
        panel  = trapezoid(
            length = self.width,
            width = self.height,
            height = self.length,
            top_width = self.outer_height
        ).rotate((0,1,0),(0,0,0),-90)
        
        self.body = panel
        
    def make_frame_cut(self):
        frame_cut  = trapezoid(
            length = self.width,
            width = self.height - self.frame*3,
            height = self.length - self.frame,
            top_width = self.outer_height - self.frame/2
        ).rotate((0,1,0),(0,0,0),-90).translate((-self.frame/2,0,0))
        
        self.frame_cut = frame_cut.translate((0,-self.width+self.frame_depth,0))
        
    def make_control_panel(self):
        control_panel = cq.Workplane("XY").box(3,1,5)
        self.control_panel = control_panel
        
    #def make_control_panel(self):
    #    control_panel = cq.Workplane("XY").box(3,1,5)
    #    self.control_panel = control_panel
        
    def make_vents(self):
        vent = cq.Workplane("XZ").cylinder(1,1)
        
        vents = (
            cq.Workplane("XY")
            .add(vent.translate((0,0,3)))
            .add(vent.translate((0,0,0)))
            .add(vent.translate((3,0,1.5)))
        )
    
        self.vents = vents
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_body()
        self.make_frame_cut()
        self.make_control_panel()
        self.make_vents()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
            
        if self.body:
            part = part.add(self.body)
            
        if self.frame_cut:
            part = part.cut(self.frame_cut.translate((0,0,0)))
            
        if self.control_panel:
            x_translate = -1
            y_translate = -self.width/2 -1/2 + self.frame_depth
            z_translate = -3
            part = part.add(self.control_panel.translate((x_translate,y_translate,z_translate)))
            
        if self.vents:
            x_translate = -2
            y_translate = -self.width/2 -1/2 + self.frame_depth
            z_translate = 2
            part = part.add(self.vents.translate((x_translate,y_translate,z_translate)))

        return part
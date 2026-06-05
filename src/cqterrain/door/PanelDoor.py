import cadquery as cq
from cadqueryhelper import Base
from cqterrain.window import frame as window_frame

class PanelDoor(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 100
        self.width:float = 5
        self.height:float = 52
        
        self.panel_count:int = 3
        
        self.render_windows:bool = True
        self.window_count:int = 2
        self.window_length:float = 12
        self.window_height:float = 6
        self.window_frame:float = 1.5
        self.window_frame_width:float = 1
        
        self.render_rollers:bool = True
        self.roller_length:float = 3
        self.roller_height:float = 4
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.panels:cq.Workplane|None = None
        self.windows_cuts:cq.Workplane|None = None
        self.windows:cq.Workplane|None = None
        self.roller_cuts:cq.Workplane|None = None
        self.rollers:cq.Workplane|None = None
        
    def calculate_panel_height(self):
        return self.height / self.panel_count
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_panels(self):
        panel_height = self.calculate_panel_height()
        
        panel = cq.Workplane("XY").box(
            self.length,
            self.width,
            panel_height
        ).faces("|Z").edges("|X").chamfer(1.5)
        
        panels = cq.Workplane("XY")
        
        for i in range(self.panel_count):
            panels = panels.add(panel.translate((0,0,panel_height*i)))
        
        self.panels = panels.translate((0,0,panel_height/2))
        
    def make_window_cuts(self):
        window = cq.Workplane("XY").box(
            self.window_length, 
            self.width, 
            self.window_height
        )
        
        window_segment_length = self.length / self.window_count
        windows = cq.Workplane("XY")
        
        for i in range(self.window_count):
            windows = windows.add(window.translate((window_segment_length*i,0,0)))
            
        
        panel_height = self.calculate_panel_height()
        z_translate = self.height - panel_height/2
        x_translate = self.length/2+ -window_segment_length/2
        
        self.window_cuts = windows.translate((-x_translate,0,z_translate))
            
        
    def make_windows(self):
        window = window_frame(
            length = self.window_length, 
            width = self.window_frame_width + self.width, 
            height = self.window_height, 
            frame_width = self.window_frame
        )
        
        window_segment_length = self.length / self.window_count
        windows = cq.Workplane("XY")
        
        for i in range(self.window_count):
            windows = windows.add(window.translate((window_segment_length*i,0,0)))
            
        
        panel_height = self.calculate_panel_height()
        z_translate = self.height - panel_height/2
        x_translate = self.length/2+ -window_segment_length/2
        
        self.windows = windows.translate((-x_translate,0,z_translate))
        
    def make_roller_cuts(self):
        panel_height = self.calculate_panel_height()
        roller = cq.Workplane("XY").box(
            self.roller_length,
            self.width,
            self.roller_height
        )
        
        rollers = cq.Workplane("XY")
        
        for i in range(self.panel_count):
            rollers = rollers.add(roller.translate((0,0,panel_height*i)))
            
        x_translate = self.length/2 - self.roller_length/2
        self.roller_cuts = (
            cq.Workplane("XY")
            .add(rollers.translate((x_translate,0,panel_height)))
            .add(rollers.translate((-x_translate,0,panel_height)))
        )
        
    def make_rollers(self):
        panel_height = self.calculate_panel_height()
        roller = cq.Workplane("YZ").cylinder(
            self.roller_length,
            self.roller_height/2
        )
        
        rollers = cq.Workplane("XY")
        
        for i in range(self.panel_count):
            rollers = rollers.add(roller.translate((0,0,panel_height*i)))
            
        x_translate = self.length/2 - self.roller_length/2
        self.rollers = (
            cq.Workplane("XY")
            .add(rollers.translate((x_translate,0,panel_height)))
            .add(rollers.translate((-x_translate,0,panel_height)))
        )
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_panels()
        self.make_window_cuts()
        self.make_windows()
        self.make_roller_cuts()
        self.make_rollers()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.panels:
            z_translate = self.height/2
            part = part.add(self.panels.translate((0,0,0)))
            
        if self.window_cuts and self.render_windows:
            part = part.cut(self.window_cuts)
            
        if self.windows and self.render_windows:
            part = part.add(self.windows)
            
        if self.roller_cuts and self.render_rollers:
            part = part.cut(self.roller_cuts)
            
        if self.rollers and self.render_rollers:
            part = part.add(self.rollers)
        
        return part
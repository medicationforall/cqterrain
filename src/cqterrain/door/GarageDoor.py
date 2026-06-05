import cadquery as cq
from cadqueryhelper import Base

from . import Frame
from . import PanelDoor
from ..greeble import BottomClamps
from ..greeble import Panel


class GarageDoor(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.render_frame:bool = True
        self.render_door:bool = True
        self.render_clamps:bool = True
        self.render_panel:bool = True

        # blueprints
        self.bp_frame:frame = self.init_frame()
        self.bp_door:PanelDoor = self.init_door()
        self.bp_clamps:BottomClamps = self.init_clamps()
        self.bp_panel:Panel = self.init_panel()
        
        #shapes
        self.outline:cq.Workplane|None = None
        
    def init_frame(self):
        bp_frame = Frame()
        bp_frame.length = 80
        bp_frame.width = 6
        bp_frame.height = 55
        
        bp_frame.frame_width = 2
        bp_frame.chamfer = 5
        bp_frame.cut_chamfer = None
        bp_frame.cut_height_mod = -3
        
        return bp_frame
    
    def init_door(self):
        bp_door = PanelDoor()
        #bp_door.length:float = 100
        bp_door.width:float = 4
        #bp_door.height:float = 52
        
        bp_door.panel_count = 3
        
        bp_door.render_windows = True
        bp_door.window_count = 2
        bp_door.window_length = 12
        bp_door.window_height = 6
        bp_door.window_frame = 1.5
        bp_door.window_frame_width = 1
        
        bp_door.render_rollers = True
        bp_door.roller_length = 3
        bp_door.roller_height = 4
        
        return bp_door
    
    def init_clamps(self):
        bp_clamps = BottomClamps()
        ##bp_clamps.length = 100
        ##bp_clamps.width = 8
        ##bp_clamps.clamp_width = 8
        
        bp_clamps.height = 2
        
        bp_clamps.clamp_height = 7
        bp_clamps.clamp_chamfer = 1
        bp_clamps.clamp_count = 3
       
        bp_clamps.clamp_bottom_length = 25
        bp_clamps.clamp_top_length = 10
        return bp_clamps
    
    def init_panel(self):
        bp_panel = Panel()
        bp_panel.length = 8
        bp_panel.width = 6
        bp_panel.height = 25
        bp_panel.outer_height = 9
        
        bp_panel.frame = 1.5
        bp_panel.frame_depth = 1
        return bp_panel
        
    def make(self):
        super().make()
        self.bp_frame.make()
        
        frame_length = self.bp_frame.calculate_cut_frame_length()
        
        self.bp_door.length = frame_length
        self.bp_door.height = self.bp_frame.calculate_cut_frame_height()
        self.bp_door.make()
        
        self.bp_clamps.length = frame_length
        self.bp_clamps.width = self.bp_frame.width
        self.bp_clamps.clamp_width = self.bp_frame.width
        self.bp_clamps.make()
        
        self.bp_panel.make()

    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bp_frame and self.render_frame:
            frame = self.bp_frame.build()
            part = part.add(frame)
            
        if self.bp_door and self.render_door:
            door = self.bp_door.build()
            part = part.union(door)
            
        if self.bp_clamps and self.render_clamps:
            clamps = self.bp_clamps.build()
            part = part.union(clamps)
            
        if self.bp_panel and self.render_panel:
            panel = self.bp_panel.build()
            
            x_translate = self.bp_frame.length/2+self.bp_panel.length/2
            y_translate = self.bp_frame.width/2 - self.bp_panel.width/2
            z_translate = self.bp_frame.height/2
            
            part = part.union(panel.translate((x_translate,y_translate,z_translate)))
        
        return part
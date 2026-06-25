import cadquery as cq
from cadqueryhelper import Base
from . import Frame
from . import DoorTwo

class DoorSingle(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 30
        self.width:float = 3
        self.height:float = 40

        self.frame_width:float = 3
        self.frame_internal_width:float = 3
        self.cut_chamfer:float = 3.5
        self.side_chamfer:float|None = None
        
        self.window_length:float = 6
        self.window_height:float = 3
        self.window_z_translate:float = 30

        # blueprints
        self.bp_frame:Base= Frame()
        self.bp_door:Base = DoorTwo()
        
        #shapes
        self.outline:cq.Workplane|None = None
        
    def calculate_internal_length(self):
        return self.length - self.frame_width * 2
    
    def calculate_internal_height(self):
        return self.height - self.frame_width
        
    def make_frame(self):
        self.bp_frame.length = self.length
        self.bp_frame.width = self.frame_internal_width
        self.bp_frame.frame_width = self.frame_width
        self.bp_frame.height = self.height
        
        self.bp_frame.make()
        
    def make_door(self):
        internal_length = self.calculate_internal_length()
        internal_height = self.calculate_internal_height()
        
        self.bp_door.length = internal_length
        self.bp_door.height = internal_height
        self.bp_door.side_chamfer = self.side_chamfer
        self.bp_door.window_length = self.window_length
        self.bp_door.window_height = self.window_height
        self.bp_door.window_z_translate = self.window_z_translate
        self.bp_door.chamfer= (self.cut_chamfer,self.cut_chamfer)
        self.bp_door.make()
        
        
    def make(self):
        super().make()
        self.make_frame()
        self.make_door()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bp_frame:
            self.bp_frame.width = self.width
            self.bp_frame.make()
            frame = self.bp_frame.build_outline()
            part = part.union(frame)
        
        z_translate = self.height/2
        return part.translate((0,0,z_translate))
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bp_frame:
            frame = self.bp_frame.build()
            part = part.union(frame)
            
            
        if self.bp_door:
            internal_length = self.calculate_internal_length()
            x_translate = -internal_length  + self.bp_door.length

            door = (
                self.bp_door.build()
                .translate((x_translate,0,0))
            )
            
            part = (
                part
                .add(door)
            )
        
        return part
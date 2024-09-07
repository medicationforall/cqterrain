import cadquery as cq
from cadqueryhelper import Base

class BaseRamp(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.length:float = 75*2
        self.width:float = 75*2
        self.height:float = 50
        
        #shapes
        self.ramp:cq.Workplane|None = None
        
    def make(self, parent=None):
        super().make(parent)
        pts = [
            (0,0),
            (self.length,0),
            (0,self.height)
        ]
        self.ramp = (
            cq.Workplane("XZ").polyline(pts).close().extrude(self.width)
        ).translate((-self.length/2,self.width/2,-self.height/2))
        
    def build(self)->cq.Workplane:
        super().build()
        if self.ramp:
            return self.ramp
        else:
            raise Exception('Unable to resolve bridge ramp')
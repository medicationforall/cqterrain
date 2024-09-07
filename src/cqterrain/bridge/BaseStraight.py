import cadquery as cq
from cadqueryhelper import Base


class BaseStraight(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.length:float = 75*2
        self.width:float = 75*2
        self.height:float = 50
        
        #shapes
        self.straight:cq.Workplane|None = None
        
    def make(self, parent=None):
        super().make(parent)
        self.straight = (
            cq.Workplane("XY").box(
                self.length,
                self.width,
                self.height
            )
        )
        
    def build(self)->cq.Workplane:
        super().build()
        if self.straight:
            return self.straight
        else:
            raise Exception('unable to resolve straight bridge section')
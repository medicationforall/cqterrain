	
import cadquery as cq
from cadqueryhelper import Base
from .SwivelBase import SwivelBase
from .SwivelTop import SwivelTop
    
class Swivel(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.channel_width:float = .8
        self.plate_x_translate:float = 40
        
        #blueprints
        self.bp_base:SwivelBase = SwivelBase()
        self.bp_top:SwivelTop = SwivelTop()
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make(self):
        super().make()
        self.bp_base.make()
        
        height = self.bp_base.calculate_cut_height()
        diameter = self.bp_base.calculate_cut_diameter()-self.channel_width*2
        
        bp_top = self.bp_top
        bp_top.diameter = diameter
        bp_top.height = height
        bp_top.make()
        
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bp_base:
            z_translate = self.bp_base.height/2
            base = self.bp_base.build()
            part = part.add(base.translate((0,0,z_translate)))
            
        if self.bp_top:
            z_translate = self.bp_base.height - self.bp_base.calculate_cut_height()
            top = self.bp_top.build()
            
            part = part.union(top.translate((0,0,z_translate)))
        
        return part
    
    def build_plate(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.bp_base:
            z_translate = self.bp_base.height/2
            base = self.bp_base.build()
            part = part.add(base.translate((0,0,z_translate)))
            
        if self.bp_top:
            z_translate = self.bp_base.height - self.bp_base.calculate_cut_height()
            top = self.bp_top.build()
            
            part = part.union(top.translate((self.plate_x_translate,0,0)))
        
        return part
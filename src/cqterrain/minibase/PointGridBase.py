import cadquery as cq
from cadqueryhelper import Base
from ..floor import ModPattern
from typing import Literal
from . import rectangle,circle,slot,ellipse,hexagon

class PointGridBase(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 30
        self.width:float = 25
        self.height:float = 3
        self.diameter:float = 30
        self.diameter_y:float = 30
        self.taper:float = -1
        self.magnet_diameter:float = 3
        self.magnet_height:float = 2
        self.render_magnet:bool = True

        self.base_type:Literal['rectangle','circle','slot','ellipse','hexagon'] = "circle"
        self.detail_height:float = 3
        self.debug:bool = False

        #blueprints
        self.bp_grid:ModPattern = ModPattern()
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.minibase:cq.Workplane|None = None
        self.top:cq.Workplane|None = None
        self.top_pattern :cq.Workplane|None = None
        
    def make_outline(self):
        length = self.length
        width = self.width
        
        if self.base_type == 'circle' or self.base_type == 'hexagon':
            length = self.diameter
            width = self.diameter
        elif self.base_type == 'ellipse':
            length = self.diameter
            width = self.diameter_y
        
        
        outline = cq.Workplane("XY").box(
            length,
            width,
            self.height+self.detail_height
        )
        
        self.outline = outline

    def make_minibase(self):
        if self.base_type == 'rectangle':
            minibase = rectangle(
                length = self.length, 
                width = self.width, 
                height = self.height, 
                taper = self.taper,
                render_magnet = self.render_magnet, 
                magnet_diameter = self.magnet_diameter, 
                magnet_height = self.magnet_height
            )
        elif self.base_type == 'circle':
            minibase = circle(
                diameter = self.diameter, 
                height = self.height, 
                taper = self.taper,
                render_magnet = self.render_magnet,
                magnet_diameter = self.magnet_diameter, 
                magnet_height = self.magnet_height
            )
        elif self.base_type == 'slot':
            minibase = slot(
                length = self.length, 
                width = self.width, 
                height = self.height, 
                taper = self.taper, 
                render_magnet = self.render_magnet,
                magnet_diameter = self.magnet_diameter, 
                magnet_height = self.magnet_height
            )
        elif self.base_type == 'ellipse':
            minibase = ellipse(
                x_diameter = self.diameter, 
                y_diameter = self.diameter_y, 
                height = self.height, 
                taper = self.taper, 
                render_magnet = self.render_magnet,
                magnet_diameter = self.magnet_diameter, 
                magnet_height = self.magnet_height
            )
        elif self.base_type == 'hexagon':
            minibase = hexagon(
                diameter = self.diameter, 
                height = self.height, 
                taper = self.taper,
                render_magnet = self.render_magnet,
                magnet_diameter = self.magnet_diameter, 
                magnet_height = self.magnet_height
            )
        else:
            raise Exception(f"Unrecognized base type {self.base_type}")
        
        self.minibase = minibase
        
        top = (
           minibase
           .faces("Z")
           .wires()
           .toPending()
           .extrude(self.detail_height)
          )
        
        self.top = top
        
        self.top_pattern  = (
           minibase
           .faces("Z")
           .wires()
           .toPending()
           .extrude(self.detail_height+5)
          )
        
    def make_grid(self):
        length = self.length
        width = self.width
        
        if self.base_type == 'circle' or self.base_type == 'hexagon':
            length = self.diameter
            width = self.diameter
        elif self.base_type == 'ellipse':
            length = self.diameter
            width = self.diameter_y
        
        self.bp_grid.length = length
        self.bp_grid.width = width
        self.bp_grid.height = self.detail_height
        self.bp_grid.make()
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_minibase()
        self.make_grid()
        
    def build_outline(self):
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            z_translate =self.height+self.detail_height 
            part.add(self.outline.translate((0,0,z_translate/2)))
        
        return part
        
    def build(self):
        super().build()
        
        part = cq.Workplane("XY")
        
        if  self.minibase:
            part = part.add(self.minibase.translate((0,0,self.height/2)))
            
        if self.bp_grid and self.top:
            grid = self.bp_grid.build()
            
            if self.debug:
                combined_pattern = (
                    cq.Workplane("XY")
                    .union(self.top.translate((0,0,self.height/2)))
                    .add(grid.translate((0,0,self.height)))
                )
                part = part.union(combined_pattern)
            else:
                combined_pattern = (
                    cq.Workplane("XY")
                    .union(self.top.translate((0,0,self.height/2)))
                    .intersect(grid.translate((0,0,self.height)))
                )
                part = part.union(combined_pattern)
            
        return part

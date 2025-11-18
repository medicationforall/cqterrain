import cadquery as cq
from cadqueryhelper import Base, irregular_grid
from typing import Literal, Callable
import random
from . import rectangle,circle,slot,ellipse,hexagon
from ..damage import uneven_plane


def custom_item(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
    )

def custom_item_rotated_y_pos(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
        .rotate((0,1,0),(0,0,0),12)
    )

def custom_item_rotated_y_neg(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
        .rotate((0,1,0),(0,0,0),-12)
    )

def custom_item_rotated_x_neg(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
        .rotate((1,0,0),(0,0,0),-6)
    )

def custom_item_rotated_x_pos(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
        .rotate((1,0,0),(0,0,0),6)
    )

class RuinStoneBase(Base):
    def __init__(self):
        super().__init__()
        #paramters
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
        
        self.uneven_height:float = 4
        self.peak_count:tuple[int,int]|int = (9,10)
        self.segments:int = 6
        self.seed:str = "seed"
        self.detail_height:float = 3
        
        self.overlap:float = 20
        self.min_height:float = 1
        self.col_size:float = 5
        self.row_size:float = 8
        self.max_columns:int = 2
        self.max_rows:int = 2
        self.passes_count:int = 3000
        self.tile_styles:list[Callable[[float, float, float],cq.Workplane]] = [
            custom_item,
            custom_item,
            custom_item,    
            custom_item_rotated_y_pos,
            custom_item_rotated_y_neg,
            custom_item_rotated_x_neg,
            custom_item_rotated_x_pos
        ]

        #shapes
        self.minibase:cq.Workplane|None = None
        self.top:cq.Workplane|None = None
        self.top_pattern :cq.Workplane|None = None
        self.uneven_plane:cq.Workplane|None = None
        self.irregular_pattern:cq.Workplane|None = None
        
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
        
    def make_uneven(self):
        length = self.length
        width = self.width
        
        if self.base_type == 'circle' or self.base_type == 'hexagon':
            length = self.diameter
            width = self.diameter
        elif self.base_type == 'ellipse':
            length = self.diameter
            width = self.diameter_y
        
        u_plane_safe = uneven_plane(
            length = length, 
            width = width,
            height = self.uneven_height,
            peak_count = self.peak_count,
            segments = self.segments,
            seed = self.seed,
            render_plate = True,
            plate_height = 0.1
        )
        
        self.uneven_plane = u_plane_safe
        
    def make_irregular(self):
        length = self.length
        width = self.width
        
        if self.base_type == 'circle' or self.base_type == 'hexagon':
            length = self.diameter
            width = self.diameter
        elif self.base_type == 'ellipse':
            length = self.diameter
            width = self.diameter_y
            
        def rand_tile(length, width, height):
            tile_style = random.choice(self.tile_styles)
            tile = tile_style(length, width, height)
            return tile
            
        irregular_pattern = irregular_grid(
            length = length + self.overlap,
            width = width + self.overlap,
            height = self.min_height,
            col_size = self.col_size,
            row_size = self.row_size,
            
            max_columns = self.max_columns,
            max_rows = self.max_rows,
            
            max_height = self.detail_height,
            align_z = True,
            include_outline = True,
            union_grid = True,
            passes_count = self.passes_count,
            seed = self.seed,
            make_item = rand_tile
        )
        
        self.irregular_pattern = irregular_pattern
            
        
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_minibase()
        self.make_uneven()
        self.make_irregular()
        
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
            
        if self.uneven_plane and self.top:
            combined_pattern = (
                cq.Workplane("XY")
                .union(self.top.translate((0,0,self.height/2)))
                .intersect(self.uneven_plane.translate((0,0,self.uneven_height/2+self.height)))
            )
            part = part.union(combined_pattern)
            
        if self.irregular_pattern and self.top_pattern:
            z_translate = self.min_height/2+self.height
            combined_irregular = (
                cq.Workplane("XY")
                .union(self.top_pattern.translate((0,0,self.height/2)))
                .intersect(self.irregular_pattern.translate((0,0,z_translate)))
            )
            
            part = part.union(combined_irregular)
        
        return part
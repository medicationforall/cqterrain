import cadquery as cq
import math
from . import BaseStraight
from ..tile import plain

class TileStraight(BaseStraight):
    def __init__(self):
        super().__init__()
        #parameters
        self.padding:float = 4
        self.tile_height:float = 4
        self.tile_length:float = 26
        self.tile_width:float = 18
        self.tile_padding:float = 1
        self.tile_method = plain

        self.base_top_margin:float = 10
        self.base_side_margin:float = 10
        self.base_fillet:float = 8
        
        self.base_inset_distance_height:float = 2
        self.base_inset_distance:float = 2
        self.base_inset_depth:float = 2
        self.base_inset_fillet:float = 9
        
        self.render_tile:bool = True
        
        #shapes
        self.tile = None
        self.tiles = None
        
    def make_tile_cut(self):
        if self.straight:
            self.straight = (
                self.straight
                .faces("Z")
                .workplane(offset=-self.tile_height/2)
                .box(
                    self.length-self.padding*2,
                    self.width-self.padding*2,
                    self.tile_height,
                    combine="cut"
                )
            )
        else:
            raise Exception("Unable to resolve straight bridge segment")
        
    def make_base_cut(self):
        base_cut = (
            cq.Workplane("XY")
            .box(
                self.length-self.base_side_margin*2,
                self.width,
                self.height - self.base_top_margin,
            )
            .faces("Z")
            .edges("Y")
            .fillet(self.base_fillet)
        )
        
        self.straight = (
            self.straight
            .cut(base_cut.translate((0,0,-self.base_top_margin/2))) #type:ignore
        )
        
    def make_base_inset(self):
        base_inset = (
            cq.Workplane("XY")
            .box(
                self.length-self.base_side_margin*2+self.base_inset_distance*2,
                self.base_inset_depth,
                self.height - self.base_top_margin+self.base_inset_distance_height,
            )
            .faces("Z")
            .edges("Y")
            .fillet(self.base_inset_fillet)
        )
        
        self.straight = (
            self.straight
            .cut(base_inset.translate(( #type:ignore
                0,
                self.width/2-self.base_inset_depth/2,
                -self.base_top_margin/2+self.base_inset_distance_height/2
            )))
            .cut(base_inset.translate((
                0,
                -self.width/2+self.base_inset_depth/2,
                -self.base_top_margin/2+self.base_inset_distance_height/2
            )))
        )
        
        
    def make_tile(self):
        self.tile = self.tile_method(
            self.tile_length,
            self.tile_width,
            self.tile_height
        )
        
    def make_tiles(self):
        x_count = math.floor((self.length-self.padding*2)/(self.tile_length+self.tile_padding*2))
        y_count = math.floor((self.width-self.padding*2)/(self.tile_width+self.tile_padding*2))
        
        
        def add_tile(loc:cq.Location)->cq.Shape:
            return self.tile.val().located(loc) #type:ignore
        
        self.tiles = (
            cq.Workplane("XY")
            .rarray(
                xSpacing = self.tile_length+self.tile_padding*2, 
                ySpacing = self.tile_width+self.tile_padding*2,
                xCount = x_count, 
                yCount= y_count, 
                center = True)
            .eachpoint(callback = add_tile)
        )
        
    def make(self, parent=None):
        super().make(parent)
        if self.straight:
            self.make_tile_cut()
            self.make_base_cut()
            self.make_base_inset()
            
            if self.render_tile:
                self.make_tile()
                self.make_tiles()
        else:
            raise Exception("Unable to resolve straight bridge segment")

        
    def build(self):
        super().build()
        if self.straight:
            scene = (
                cq.Workplane("XY")
                .add(self.straight)
            )
            
            if self.render_tile and self.tiles:
                scene = scene.add(self.tiles.translate((0,0,self.height/2-self.tile_height/2)))
            return scene
        else:
            raise Exception("Unable to resolve straight bridge segment")
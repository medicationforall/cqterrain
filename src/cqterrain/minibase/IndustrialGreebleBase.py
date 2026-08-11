import cadquery as cq
from cadqueryhelper import Base
from . import RuinStoneBase
from .. import tile as terrain_tile,greeble
import math
from typing import Callable

# ---------- Custom Tiles

def _vent_greeble(length, width, height):
    t = greeble.vent(length, width, height ,inner_width = height-1,)
    return t


def _round_plate(length, width, height):
    if length == width:
        t = terrain_tile.rivet_round(
            radius = length/2, 
            height = height,
            rivet_height = 0.5,
            rivet_radius = .5,
            padding = 0,
            rivet_count = math.floor(length/2)
        )

    else:
        #t = greeble.vent(length, width, height ,inner_width = height-1,)
        t = terrain_tile.bolt_panel(length,width,height, padding = 1.5)
    return cq.Workplane("XY").union(t)

def _conduit(length, width, height):
    result = terrain_tile.conduit(
        length = length,
        width = width,
        height = height,
        frame= 1,
        frame_depth = height - 0.5,
        pipe_count = None,
        radius = 2,
        inner_radius = 1,
        segment_length = 5,
        space = 2.5,
        pipe_padding = .5
    )
    
    return result

#-------------------

class IndustrialGreebleBase(RuinStoneBase):
    def __init__(self):
        super().__init__()
        #parameters
        self.render_uneven:bool = False
        self.detail_height:float = 2
        self.max_columns:int = 2
        self.max_rows:int = 2
        self.col_size:float = 10
        self.row_size:float = 10
        self.tile_styles:[Callable[float,float,float]] =[
            _round_plate,
            _vent_greeble,
            terrain_tile.bolt_panel,
            terrain_tile.plain,
            terrain_tile.slot,
            #terrain_tile.charge,
            _conduit
        ]
        
    def make(self):
        super().make()
        
    def build(self)->cq.Workplane:
        return super().build()
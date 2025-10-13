import cadquery as cq
from . import ellipse
from ..floor import WoodFloor

def ellipse_wood(
    x_diameter:float = 52, 
    y_diameter:float = 90, 
    base_height:float = 3,
    taper:float = -1,
    render_magnet:bool = True,  
    magnet_diameter:float = 3, 
    magnet_height:float = 2,
    board_height:float = 1,
    overlap:float = 20,
    seed:str = "seed",
    joist_space:float = 12.5,
    board_width:float = 6.5,
    board_width_spacer:float = .2,
    board_break_width:float = .4,
    nail_diameter:float = .6,
    nail_overlap_height:float = .4,
    joist_width:float = 4,
    debug:bool = False
):
    mini_base = ellipse(
        x_diameter = x_diameter,
        y_diameter = y_diameter,
        height = base_height, 
        taper = taper,
        render_magnet = render_magnet,  
        magnet_diameter = magnet_diameter, 
        magnet_height = magnet_height
    )
    
    greeble_floor_height = board_height+1
    
    top = (
       mini_base
       .faces("Z")
       .wires()
       .toPending()
       .extrude(greeble_floor_height)
    )
    
    bp_floor = WoodFloor()
    bp_floor.length= x_diameter + overlap
    bp_floor.width= y_diameter + overlap
    bp_floor.height = 4
    
    #joist
    bp_floor.joist_width = joist_width
    bp_floor.joist_space = joist_space
    bp_floor.joist_count= 4
    bp_floor.render_joists= False
    
    # Board
    bp_floor.board_width= board_width
    bp_floor.board_width_spacer = board_width_spacer
    bp_floor.board_height = board_height = 1.5
    
    #nail
    bp_floor.nail_diameter = nail_diameter
    bp_floor.nail_overlap_height = nail_overlap_height
    bp_floor.nail_x_margin = .5
    bp_floor.nail_y_margin = .5
    
    # grid
    bp_floor.seed= seed
    bp_floor.board_lengths = [1,4]
    bp_floor.board_break_width= board_break_width
    bp_floor.grid = []
    
    bp_floor.make()
    
    z_translate = board_height/2 + base_height/2
    ex_floor = bp_floor.build().translate((0,0,z_translate))
    
    if debug:
        return mini_base.add(ex_floor).add(top)
    else:
        greeble_floor = ex_floor.intersect(top)
        return mini_base.union(greeble_floor)
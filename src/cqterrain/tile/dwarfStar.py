import cadquery as cq
from cadqueryhelper.shape import diamond

def dwarf_star(
        length:float = 15,
        width:float = 15,
        height:float = 2,
        depth:float = .6, 
        margin:float = .6,
        inner_band_width:float = 1,
        inner_track_width:float = 1
    ) -> cq.Workplane:
    tile = (
        cq.Workplane("XY")
        .box(length,width,height)
    )
    
    margin_cut = (
        cq.Workplane("XY")
        .box(length,width,depth)
        .box(length-margin*2,width-margin*2,depth, combine='cut')
    )
    
    inner_track = (
        cq.Workplane("XY")
        .box(
            length-margin*2-inner_band_width*2,
            width-margin*2-inner_band_width*2,
            depth
        )
    )
    
    track_diamond = diamond(
        length-margin*2,
        width-margin*2,
        depth
    )
    
    inner_box = (
        cq.Workplane("XY")
        .box(
                length-margin*2-inner_band_width*2-inner_track_width*2,
                width-margin*2-inner_band_width*2-inner_track_width*2,
                depth
        )
    )
    
    return (
        tile
        .cut(margin_cut.translate((0,0,height/2-depth/2)))
        .cut(inner_track.translate((0,0,height/2-depth/2)))
        .cut(track_diamond.translate((0,0,height/2-depth/2)))
        .union(inner_box.translate((0,0,height/2-depth/2)))
    )
import cadquery as cq
from cqterrain import Ladder


def _make_rung(length, width, height):
    rung = cq.Workplane("XY").box(length+1.5, width ,height)
    rung = rung.edges("X").fillet(.909999)
    return rung

def _make_side_rail(width, height, rail_width):
    rail = (cq.Workplane("XY")
            .box( height, rail_width, width)
            .rotate((0,0,1),(0,0,0),90)
            .rotate((1,0,0),(0,0,0),90)
            )
    rail = rail.faces("<Y").edges("X").fillet(3)
    return rail

ladder_bp = Ladder()
ladder_bp.make_rung = _make_rung
ladder_bp.make_side_rail = _make_side_rail
ladder_bp.make()
ladder = ladder_bp.build()

#show_object(ladder)
cq.exporters.export(ladder,'out/ladder.stl')

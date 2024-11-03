import cadquery as cq
from typing import List

def center_blocks(blocks:cq.Workplane) -> List[cq.Workplane]:
    split_blocks = blocks.solids().vals()
    c_blocks = []
    for s_block in split_blocks:
        bound_center = s_block.CenterOfBoundBox() #type:ignore
        location = cq.Location((-bound_center.x,-bound_center.y,0))
        scene = cq.Workplane("XY").add(s_block.located(location)) #type:ignore
        c_blocks.append(scene)
    return c_blocks
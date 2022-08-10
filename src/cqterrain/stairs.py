import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import series
import math


def __make_rail(length, height, run, rail_width, rail_height):
    rail_length = length-run
    bookend_length = (length - rail_length) / 2
    rail = shape.rail(length = rail_length, width = rail_width, height = height, inner_height = rail_height)

    rail_assembly = cq.Assembly()
    rail_assembly.add(rail, name="r_rail", loc=cq.Location(cq.Vector(0, 0, 0)))

    if bookend_length > 0:
        print('append rail ends')
        end = shape.cube(bookend_length, rail_width, rail_height)
        rail_assembly.add(end, name="top", loc=cq.Location(cq.Vector((rail_length/2)+(bookend_length/2), 0, (height/2)-(rail_height/2))))
        rail_assembly.add(end, name="bottom", loc=cq.Location(cq.Vector(-1*((rail_length/2)+(bookend_length/2)), 0, -1*((height/2)-(rail_height/2)))))


    comp_rail = rail_assembly.toCompound()
    return comp_rail

def make_stairs(length=30, width=10, height=30,  run = 5, stair_length_offset=0, stair_height = 1, rail_width = 1, rail_height = 5, step_overlap=None):
    stair_repeat = math.floor(length / (run + stair_length_offset))
    rise = (height - (stair_repeat * stair_height)) / stair_repeat

    rail = __make_rail(length, height, run, rail_width, rail_height)

    if step_overlap == None:
        step_overlap = rail_width/2
        
    step = shape.cube(length = run, width = (width-(rail_width*2) + (step_overlap*2)), height = stair_height)
    steps = series.make_series(shape = step, size = stair_repeat, length_offset = stair_length_offset, height_offset = rise)

    stair_assembly = cq.Assembly()
    stair_assembly.add(rail, name="r_rail", loc=cq.Location(cq.Vector(0, -1*(rail_width/2), 0)))
    stair_assembly.add(steps, name="steps", loc=cq.Location(cq.Vector(0, -1*((width)/2), 0)))
    stair_assembly.add(rail, name="l_rail", loc=cq.Location(cq.Vector(0, -1*(width-(rail_width/2)), 0)))

    comp_stairs = stair_assembly.toCompound()

    # center shape
    ##comp_stairs = comp_stairs.translate((0,(width/2),0))

    meta = {'type':'stairs', 'height':0, 'length':0, 'width':0}
    comp_stairs.metadata = meta

    # todo I need to center along the y axis

    return comp_stairs

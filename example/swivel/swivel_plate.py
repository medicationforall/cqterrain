import cadquery as cq
from cqterrain.swivel import Swivel

bp = Swivel()
bp.channel_width = .8
bp.plate_x_translate = 40

bp.make()
ex_plate = bp.build_plate()

#show_object(ex_plate)
cq.exporters.export(ex_plate,"stl/swivel_plate.stl")
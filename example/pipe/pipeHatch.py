import cadquery as cq
from cqterrain import pipe
from cqterrain.barrier import (
    cut_magnets
)

con_height = 4
con = pipe.connector(
    length = con_height, 
    radius = 11.5, 
    face_height = 23
)

h_ex = pipe.hatch(
    con,
    height=con_height
).rotate((0,1,0),(0,0,0),-90).translate((0,0,12)).rotate((0,0,1),(0,0,0),180)

hatch_magnets = cut_magnets(
        h_ex,
        y_offset = 0,
        z_lift = 6,
        x_plus_cut = True,
        x_minus_cut = False,
        debug=False
    )

straight = (
    pipe
    .straight(debug_magnets=False)
    .translate((-45,0,0))
)


#show_object(hatch_magnets.rotate((0,0,1),(0,0,0),180))

cq.exporters.export(hatch_magnets,"stl/pipe_hatch.stl")

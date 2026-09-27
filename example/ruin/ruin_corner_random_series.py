import cadquery as cq
from cqterrain.ruin import ruin_corner_random

series = cq.Workplane("XY")


for i in range(10):
    
    ruin = ruin_corner_random(
        length = 50, 
        width = 50, 
        height = 10, 
        points = 7,
        debug = False,
        shift = (-4,5,1),
        seed = f"ruin_{i}"
    )
    
    series = series.add(ruin.translate((-(i*3),0,i*(10+2))))

#show_object(series)
cq.exporters.export(series,"stl/ruin_corner_random_series.stl")
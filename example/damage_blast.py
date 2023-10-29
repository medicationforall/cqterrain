import cadquery as cq
from cqterrain import damage 

blast_ex = damage.blast(
    seed="test",
    height=10,
    count = (5,10),
    x_jiggle = (-2,2), 
    y_jiggle = 0,
    ring_params = [
        {"radius":(35,50), "start_angle":0}, 
        {"radius":25,"start_angle":30}
    ]
)

blast_ex2 = damage.blast(
    seed="test2",
    height=10,
    count = 9,
    x_jiggle = (-2,10), 
    y_jiggle = (-2,10),
    ring_params = [
        {"radius":50, "start_angle":0}, 
        {"radius":40,"start_angle":0}
    ]
)

blast_ex3 = damage.blast(
    seed="t2",
    height=10,
    count = (8,12),
    x_jiggle = (-4,5), 
    y_jiggle = (-5,4),
    ring_params = [
        {"radius":(40,50), "start_angle":0}, 
        {"radius":35,"start_angle":0}
    ]
)

cq.exporters.export(blast_ex, "out/damage_blast_1.stl")
cq.exporters.export(blast_ex2, "out/damage_blast_2.stl")
cq.exporters.export(blast_ex3, "out/damage_blast_3.stl")
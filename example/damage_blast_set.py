import cadquery as cq
from cqterrain import damage 

blasts = cq.Workplane("XY")
row_count = -1
for i in range(20):
    blast_seed = f"blast{i}"
    f_blast = damage.blast(
        seed = blast_seed,
        height=10,
        count = (4,12),
        x_jiggle = (-4,5), 
        y_jiggle = (-5,4),
        ring_params = [
            {"radius":(40,50), "start_angle":0}, 
            {"radius":(20,35),"start_angle":10}
        ]
    )
    col_count = i % 5
    if col_count == 0:
        row_count += 1
    text = cq.Workplane("XY").text(blast_seed,14, 2)
    blasts.add(f_blast.translate((100*col_count,-100*row_count,0)))
    blasts.add(text.translate((100*col_count,-100*row_count,5)))

cq.exporters.export(blasts, "out/damage_blast_set.stl")

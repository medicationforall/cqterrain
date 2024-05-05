import cadquery as cq
from cadqueryhelper import shape
import random
from cqterrain import damage

def blast_template(blast_seed):
    f_blast = damage.blast(
        seed = blast_seed,
        height=10,
        count = (4,14),
        x_jiggle = (-4,5), 
        y_jiggle = (-5,4),
        ring_params = [
            {"radius":(40,50), "start_angle":0}, 
            {"radius":(20,35),"start_angle":10}
        ]
    )
    text = cq.Workplane("XY").text(blast_seed,14, 2)
    return f_blast, text
    
blasts = damage.grid_seed(
    blast_template,
    count = 24, 
    seed_base = "blast", 
    columns = 7,
    length = 100,
    width = 100,
    z_transform = 5
)

#show_object(blasts)
cq.exporters.export(blasts, "stl/damage_blast_set_large.stl")
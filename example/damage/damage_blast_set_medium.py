import cadquery as cq
from cadqueryhelper import shape
from cqterrain import damage

def blast_template(blast_seed:str) -> tuple[cq.Workplane, cq.Workplane]:
    f_blast = damage.blast(
        seed = blast_seed,
        height=5,
        count = (4,14),
        x_jiggle = (-2,3), 
        y_jiggle = (-3,2),
        ring_params = [
            {"radius":(20,25), "start_angle":0}, 
            {"radius":(10,18),"start_angle":10}
        ]
    )
    text = cq.Workplane("XY").text(blast_seed,6, 2)
    return f_blast, text

test_seed = "med"    
blasts = damage.grid_seed(
    blast_template,
    count = 24, 
    seed_base = "med", 
    columns = 8
)

#show_object(blasts)
cq.exporters.export(blasts, f"stl/damage_blast_set_medium_{test_seed}.stl")
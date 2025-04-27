import cadquery as cq
from cqterrain.crystal import crystal_random

def crystal_adder():
    # closure
    count = 0
    def add_crystal(loc:cq.Location)->cq.Shape:
        nonlocal count
        count += 1
        adder_seed = f"blue_{count}"
        crystal,crystal_height = crystal_random(
            height = (50,75,2.5), 
            base_height = 0.5,
            inset_height = (5.0,10.0,1.0),
            mid_height = (1.0,10.0,1.0),
            mid_width = (20,25.0,2.5),
            top_height=(20,65,5),
            seed=adder_seed,
            faces=(4,10,1),
            intersect = True
        )
        
        crystal = crystal.translate((0,0,crystal_height/2)).union(cq.Workplane("XY").text(adder_seed,10,5).translate((0,25,30)))
        return crystal.val().located(loc) #type:ignore
    return add_crystal

size = 5
group = (
    cq.Workplane("XY")
    .rarray(
    xSpacing = 50, 
    ySpacing = 50,
    xCount = size, 
    yCount= size,
    center = True)
    .eachpoint(crystal_adder())
)


# show_object(model)
cq.exporters.export(group,'stl/crystal_random_group.stl')
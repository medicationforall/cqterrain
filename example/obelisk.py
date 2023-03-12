import cadquery as cq
from cqterrain import obelisk

fantasy = obelisk(
    height=105
)

elven = obelisk(
    height=105,
    faces=6,
    intersect=True
)

fantasy_elven = (
    fantasy
    .union(elven)
    .union(elven.rotate((0,0,1),(0,0,0),90))
)

egypt = obelisk(
    base_width=30,
    base_height=5,
    inset_width=25,
    mid_width=25,
    mid_height=5,
    height=105
)

dwarven = obelisk(
    base_width=30,
    base_height=5,
    inset_width=25,
    mid_width=25,
    mid_height=5,
    height=105,
    faces=6,
    intersect=True
)

egypt_dwarven = (
    egypt
    .union(dwarven)
    .union(dwarven.rotate((0,0,1),(0,0,0),90))
)

crystal = obelisk(
    base_width=30,
    base_height=5,
    inset_width=10,
    mid_width=15,
    mid_height=5,
    top_width=40,
    height=105,
    faces=6,
    intersect=True
)

evile = obelisk(
    base_width=40,
    base_height=3,
    inset_width=50,
    mid_width=5,
    mid_height=15,
    top_width=60,
    top_height=40,
    height=105,
    faces=8,
    intersect=False
)

cq.exporters.export(fantasy,'out/obelisk_fantasy.stl')
cq.exporters.export(elven,'out/obelisk_elven.stl')
cq.exporters.export(fantasy_elven,'out/obelisk_fantasy_elven.stl')

cq.exporters.export(egypt,'out/obelisk_egypt.stl')
cq.exporters.export(dwarven,'out/obelisk_dwarven.stl')
cq.exporters.export(egypt_dwarven,'out/obelisk_egypt_dwarven.stl')

cq.exporters.export(crystal,'out/obelisk_crystal.stl')
cq.exporters.export(evile,'out/obelisk_evile.stl')

scene = (
    cq.Workplane("XY")
    .union(fantasy)
    .union(elven.translate((-40,0,0)))
    .union(fantasy_elven.translate((-80,0,0)))
    .union(egypt.translate((0,40,0)))
    .union(dwarven.translate((-40,40,0)))
    .union(egypt_dwarven.translate((-80,40,0)))
    .union(crystal.translate((0,80,0)))
    .union(evile.translate((0,145,0)))
)

cq.exporters.export(scene,'out/obelisk_plate.stl')

#show_object(scene)

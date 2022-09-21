import cadquery as cq
from cqterrain import Building, Room

def make_entrance():
    bp = Building(length=75, width=75, height=75, stories=1)
    bp.room['build_walls']= [True,False,True,True]
    bp.room['door_walls'] = [False, False, True, False]
    bp.room['window_walls'] = [True, False, False, False]
    bp.room['window_count'] = 2
    bp.make()

    bp.floors[0].window['padding'] = 5
    bp.floors[0].window['height'] = 35
    bp.floors[0].window['length'] = 20
    bp.floors[0].door['length']=35
    bp.floors[0].make()

    entrance = bp.build().translate((0,75,0))
    return entrance

def make_roof():
    bp = Room(
        length=75,
        width=75,
        height=20,
        build_walls = [True, False, True, True],
        window_walls = [False, False, False, False],
        door_walls = [False, False, False, False],
        )
    bp.make()
    roof = bp.build()
    roof = roof.translate((0,75,10+37.5))
    return roof


def make_tower():
    building_bp = Building(length=75, width=75, height=150, stories=2)
    building_bp.room['build_walls']= [True,True,True,False]
    building_bp.room['door_walls'] = [True, False, False, False]
    building_bp.room['window_walls'] = [False, True, True, False]
    building_bp.room['window_count'] = 3
    building_bp.make()
    building = building_bp.build()
    return building

def make_tower2():
    bp = Building(length=75, width=75, height=150, stories=2)
    bp.room['build_walls']= [True,True,False,True]
    bp.room['window_count'] = 3
    bp.make()

    bp.floors[0]
    bp.floors[0].door_walls = [False, False, False, True]
    bp.floors[0].window_walls = [True, True, False, False]
    bp.floors[0].door['length']=35
    bp.floors[0].make()

    building = bp.build()
    building  = building.translate((-75,0,0))
    return building


tower = make_tower()
tower1_roof = make_roof().translate((0,-75,75)).rotate((0,0,1),(0,0,0),90)
tower= cq.Workplane("XY").add(tower).add(tower1_roof)

tower2 = make_tower2()
tower2_roof = make_roof().translate((0,0,75)).rotate((0,0,1),(0,0,0),-90)
tower2= cq.Workplane("XY").add(tower2).add(tower2_roof)

entrance = make_entrance()
entrance_roof = make_roof()
entrance= cq.Workplane("XY").add(entrance).add(entrance_roof)

scene = cq.Workplane("XY").add(tower).add(tower2).add(entrance)

#show_object(scene)
cq.exporters.export(scene,'out/deadzone_building.stl')


#show_object(tower2)
#show_object(tower2.translate((75,-85,0)))
#show_object(entrance)

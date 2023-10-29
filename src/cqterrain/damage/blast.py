import cadquery as cq
from cadqueryhelper import shape
import random

def random_nudge_points(
        seed, 
        points, 
        x_jiggle = (-2,8), 
        y_jiggle = (-1,1)
    ):
    random.seed(seed)
    mod_points = []
    for point in points:
        if type(x_jiggle) is tuple:
            r_x = random.randrange(x_jiggle[0], x_jiggle[1])
        else: 
            r_x = x_jiggle
            
        if type(y_jiggle) is tuple:
            r_y = random.randrange(y_jiggle[0], y_jiggle[1])
        else: 
            r_y = y_jiggle
            
        new_point = (point[0]+r_x,point[1]+r_y)
        mod_points.append(new_point)
        
    return mod_points

def blast(
        seed="test",
        height = 3,
        count = (5,10),
        x_jiggle = (-2,8), 
        y_jiggle = (-1,1),
        ring_params = [
            {"radius": 30, "start_angle":0}, 
            {"radius":20,"start_angle":8}
        ]
    ):
    random.seed(seed)
    point_count = count
    
    if type(point_count) is tuple:
        point_count = random.randrange(count[0], count[1])
    
    point_lists = []
    for ring_param in ring_params:
        arc_radius = ring_param["radius"]
        
        if type(arc_radius) is tuple:
            arc_radius = random.randrange(arc_radius[0], arc_radius[1])
        
        arc, tuple_points = shape.make_circular_points(
            radius = arc_radius, 
            startAngle=ring_param["start_angle"], 
            count = point_count
        )
        point_lists.append(tuple_points)
        
    points = shape.interweave_lists(point_lists)
    points = random_nudge_points(seed, points, x_jiggle, y_jiggle)
    
    result = cq.Workplane("XY").polyline(points).close()
    
    if height:
        return result.extrude(height).translate((0,0,-1*(height/2)))
    else:
        return result
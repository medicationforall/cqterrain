# Copyright 2023 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cadquery as cq
from cadqueryhelper import shape
import random

def random_nudge_points(
        seed:str, 
        points, 
        x_jiggle:tuple[int,int]|int = (-2,8), 
        y_jiggle:tuple[int,int]|int = (-1,1)
    ) -> list[tuple[int,int]]:
    random.seed(seed)
    mod_points:list[tuple[int,int]] = []
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
        seed:str = "test",
        height:float = 3,
        count:tuple[int,int]|int = (5,10),
        x_jiggle:tuple[int,int]|int = (-2,8), 
        y_jiggle:tuple[int,int]|int = (-1,1),
        ring_params:list[dict] = [
            {"radius": 30, "start_angle":0}, 
            {"radius":20,"start_angle":8}
        ]
    ) -> cq.Workplane:
    random.seed(seed)
    point_count:int = count #type:ignore
    
    if type(point_count) is tuple:
        point_count = random.randrange(count[0], count[1]) #type:ignore
    
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
# Copyright 2025 James Adams
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
from cadqueryhelper import Base
from cadqueryhelper.shape import ring
from typing import Literal, Tuple
import math


def rotate_point(point, angle=0, origin = (0,0)):
    """
    https://stackoverflow.com/a/34374437
    Rotate a point clockwise by a given angle degrees around a given origin.
    """
    o_x, o_y = origin
    p_x, p_y = point
    angle = -math.radians(angle)

    q_x = o_x + math.cos(angle) * (p_x - o_x) - math.sin(angle) * (p_y - o_y)
    q_y = o_y + math.sin(angle) * (p_x - o_x) + math.cos(angle) * (p_y - o_y)
    
    return (q_x, q_y)


def condition_points(pts):
    length = len(pts)
    
    if length > 2:
        return pts
    else:
        # https://www.calculatorsoup.com/calculators/geometry-plane/midpoint-calculator.php
        mx = (pts[0][0] + pts[1][0])/2
        my = (pts[0][1] + pts[1][1])/2
        
        mid_point = (mx,my) 
        pts.insert(1,mid_point )
    return pts

class CircuitGlyph(Base):
    def __init__(self):
        super().__init__()
        #paramters
        self.length:float = 30
        self.width:float = 25
        self.height:float = 3
        self.point_diameter:float = 3
        self.line_width:float = .5
        self.line_height:float = 1
        self.kind:Literal['arc', 'intersection', 'tangent'] = 'arc'
        
        self.pts:list[Tuple[int,int]] = []
        self.render_outline:bool = False
        self.outline_margin:float = 0
        self.debug:bool = False
        
        #shapes
        self.outline = None
        self.points = None
        self.points_outline = None
        self.connection = None
        self.point_shapes:list[cq.Workplane|None] = []
        
    def add_point(self,x=0,y=0,shape=None):
        """
        Absolute point placement
        """
        pt = (x,y)
        self.pts.append(pt)
        
        if shape:
            self.point_shapes.append(shape)
        else:
            self.point_shapes.append(None)

    def add_point_rotate(self, x, y, angle, shape=None):
        """
        Relative point placement
        """
        pt = (x,y)
        prev_pt = (0,0)

        if len(self.pts)>0:
            prev_pt = self.pts[-1]
            pt = (x+prev_pt[0],y+prev_pt[1])

        r_pt = rotate_point(pt, angle, prev_pt)
        self.pts.append(r_pt)

        if shape:
            self.point_shapes.append(shape)
        else:
            self.point_shapes.append(None)

    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline

    def make_connection(self):
        connection = cq.Workplane("XY")
        
        if len(self.pts)>1:
            pts = condition_points(self.pts)
            
            connection = (
                connection
                .polyline(pts)
                .offset2D(self.line_width/2, self.kind)
                .extrude(self.line_height)
                .translate((0,0,-self.line_height/2))
            )
            
            self.connection = connection
        
    #def make_connection_2(self):
    #    connection = cq.Workplane("XY")
    #    
    #    if len(self.pts)>1:
    #        pts = condition_points(self.pts)
    #
    #        origin = pts[0]
    #        connection = connection.center(origin[0],origin[1])
    #
    #        for pt in pts[1:]:
    #            connection = connection.lineTo(pt[0],pt[1])
    #        
    #        connection = (
    #            connection
    #            .offset2D(self.line_width/2, self.kind)
    #            .extrude(self.line_height)
    #            .translate((0,0,-self.line_height/2))
    #        )
    #       
    #        self.connection = connection
        
    def make_points(self):
        points = cq.Workplane("XY")
        nonpoints = cq.Workplane("XY")
        
        for i,pt in enumerate(self.pts):
            #log("add point")
            
            if self.point_shapes[i]:
                #log("add custom point")
                point_shape:cq.Workplane = self.point_shapes[i] #type:ignore
                diameter = self.point_diameter
                
                bounds = point_shape.val().BoundingBox() #type:ignore
                x_len = bounds.xlen
                y_len = bounds.ylen
                
                diameter = x_len
                if x_len > y_len:
                    diameter = y_len
                    
                
                points = points.add(point_shape.translate((pt[0],pt[1],0)))
                nonpoint = cq.Workplane("XY").cylinder(self.height,diameter/2 + self.outline_margin)
                nonpoints.add(nonpoint.translate((pt[0],pt[1],0)))

        self.points = points
        self.points_outline = nonpoints
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_points()
        self.make_connection()
        
    def build(self):
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline and self.render_outline:
            part = part.add(self.outline)
            
        if self.points:
            part = part.union(self.points)#.add(self.outline))
            
        if self.connection and self.points_outline:
            connection = self.connection.cut(self.points_outline)
            part = part.union(connection.translate((0,0,self.height/2 - self.line_height/2)))
            
        if self.debug:
            tp = []
            
            for i in self.pts:
                tp.append(i)
            
            con2 = cq.Workplane("XY").polyline(tp)
            #show_object(con2)
            #show_object(con2.offset2D(self.line_width/2, self.kind))
        
        return part
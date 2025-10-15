import cadquery as cq
from cadqueryhelper import Base
from cadqueryhelper.shape import ring
from typing import Literal, Tuple

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
        self.kind:Literal['arc', 'intersection', 'tangent'] = 'intersection'
        
        self.pts:list[Tuple[int,int]] = []
        self.render_outline:bool = False
        
        #shapes
        self.outline = None
        self.points = None
        self.points_outline = None
        self.connection = None
        self.point_shapes:list[cq.Workplane|None] = []
        
    def add_point(self,x=0,y=0,shape=None):
        pt = (x,y)
        self.pts.append(pt)
        
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
                nonpoint = cq.Workplane("XY").cylinder(self.height,diameter/2)
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
            
        tp = []
        
        for i in self.pts:
            tp.append(i)
        
        con2 = cq.Workplane("XY").polyline(tp)
        #show_object(con2)
        
        return part
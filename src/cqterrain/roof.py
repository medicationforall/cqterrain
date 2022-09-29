import cadquery as cq
from cadqueryhelper import grid
import math

def hip(length= 40, width=40, top=0, left=0, right=0, height=40):
    top_r = top /2
    max_w = width/2
    max_l = length/2
    roof = cq.Workplane("XY" ).wedge(length,height,width,max_l-top_r-left,max_w-top_r,max_l+top_r+right,max_w+top_r).rotate((1,0,0), (0,0,0), -90)
    return roof

def shell(part, face="-Z", width=-1):
    result = part.faces(face).shell(width)
    return result

def angle(length, height):
    '''
    Presumed length and height are part of a right triangle
    '''
    hyp = math.hypot(length, height)
    angle = length/hyp
    angle_radians = math.acos((angle))
    angle_deg = math.degrees(angle_radians)
    return angle_deg


def tiles2(tile, face, x, height, t_length, t_width, angle, odd_col_push = [0,0], rows=3):
    hyp = math.hypot(x, height)
    columns = math.floor(hyp / t_length)+4
    #rows = math.floor(height / t_width)+3

    c_face = face
    plane = (c_face.wires()
             .toPending()
             .translate((3, 0, 0.0))
             .toPending()
             .loft()
             )
    tiles = (grid.make_grid(tile, [t_length, t_width], rows=rows, columns=columns, odd_col_push=odd_col_push)
             .rotate((0,1,0),(0,0,0),-angle)
             .translate(((x/4),0,0))
             )

    combine = tiles.intersect(plane)
    return combine

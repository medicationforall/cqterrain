import cadquery as cq
from cqterrain import roof
import math

length= 40
width = 50
height = 50
tile_rows = 14
t_length = 4
t_width = 4
t_height = 0.5
t_rotation = 8

roof_ex = roof.hip(length=length, width=width, height=height)
s_roof = roof.shell(roof_ex, "-Z", -1)

tile = cq.Workplane("XY").box(t_length,t_width,t_height).rotate((0,1,0),(0,0,0),t_rotation)

angle_x = roof.angle(length/2, height)
face_x = s_roof.faces(">X")

angle_y = roof.angle(width/2, height)
face_y = s_roof.rotate((0,0,1),(0,0,0),90).faces(">X")


tiles = roof.tiles2(tile, face_x, length, height, t_length, t_width, angle_x, rows=tile_rows, odd_col_push=[1,0])
tiles3 = roof.tiles2(tile, face_y, width, height, t_length, t_width, angle_y, rows=tile_rows, odd_col_push=[-1,0]).rotate((0,0,1),(0,0,0),90)

tiles4 = roof.tiles2(tile, face_y, width, height, t_length, t_width, angle_y, rows=tile_rows, odd_col_push=[-1,0]).rotate((0,0,1),(0,0,0),-90)
tiles2 = roof.tiles2(tile, face_x, length, height, t_length, t_width, angle_x, rows=tile_rows, odd_col_push=[-1,0]).rotate((0,0,1),(0,0,0),180)

scene = s_roof.add(tiles).add(tiles2).add(tiles3).add(tiles4)
#show_object(scene)
cq.exporters.export(scene,'out/roof.stl')

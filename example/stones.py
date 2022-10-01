import cadquery as cq
import random
from cqterrain import stone
from cadqueryhelper import grid
import math


tile = cq.Workplane("XY").box(5,5,2)
tile2 = cq.Workplane("XY").box(4,4,2)
tile3 = cq.Workplane("XY").box(3,6,2)
tiles = stone.make_stones([tile.chamfer(0.8), tile2.fillet(.5), tile3.chamfer(0.5)], [6,6,2], columns = 10, rows = 3)

#show_object(tiles)
cq.exporters.export(tiles,'out/stones.stl')

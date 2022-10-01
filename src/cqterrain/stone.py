
import cadquery as cq
import random
import math

def make_stones(parts, dim=[5,5,2], rows=2, columns = 5, seed="test4"):
    grid = cq.Assembly()
    random.seed(seed)

    for row_i in range(rows):
        row_offset = (dim[0] * row_i)
        for col_i in range(columns):
            col_offset = (dim[1] * col_i)

            col_push_x = 0
            col_push_y = 0
            if col_i % 2 == 1:
                col_push_x = 0
                col_push_y = 0

            z_push = random.randrange(-1*math.floor(dim[2]),math.floor(dim[2]))
            z_push=0
            x_rand = random.randrange(-1*(math.floor(dim[0]/2)),(math.floor(dim[0]/2)))
            y_rand = random.randrange(-1*(math.floor(dim[1]/2)),(math.floor(dim[1]/2)))
            part_index = random.randrange(0,len(parts))
            grid.add(parts[part_index], loc=cq.Location(cq.Vector(row_offset + col_push_x + x_rand, col_offset + col_push_y + y_rand, z_push)))

    length = dim[1] * columns
    width = dim[0] * rows

    comp = grid.toCompound()
    work = cq.Workplane("XZ").center(0, 0).workplane()
    work.add(comp)

    # zero out the grid
    work = work.translate(((dim[0]/2),(dim[1]/2)))
    work = work.translate((-1*(width/2),-1*(length/2)))
    return work

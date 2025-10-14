import cadquery as cq
from cqterrain.greeble import CircuitGlyph 
from cadqueryhelper.shape import ring

log = print

def make_collision_map(x_count = 5, y_count = 5):
    grid_map = []
    total_cells = x_count * y_count
    cell_count = 0
    row_count = -1
    
    row_list = []
    
    for i in range(total_cells):
        if cell_count % x_count == 0:
            cell_count = 0
            row_count += 1
            
            if row_count:
                grid_map.append(row_list)
            row_list = []
        
        row_list.append(False)
        #grid = grid.add(cell.translate((10*cell_count,10*row_count,0)))
        
        cell_count+=1
        
    grid_map.append(row_list)
    
    return grid_map

def create_points_three(bp_glyph, grid_map, cell_count, x = -1, y = 0,dir = "left"):
    #log(f"create_points_three {cell_count=} {x=} {y=} {dir=}")
    directions = ["left","up","right","down"]
    
    row_bound = len(grid_map)
    col_bound = len(grid_map[0])
    cell_ring = ring(4,2,3)
    
    if cell_count:
        old_cell_count = cell_count
        cell_count-=1
        
        #bound check
        #log(f"modify bounds {dir}")
        old_x = x
        old_y = y
        
        if dir == "left":
            x+=1
        elif dir == "up":
            y+=1
        elif dir == "right":
            x-=1
        elif dir == "down":
            y-=1
    
        if x < col_bound and x > -1 and y < row_bound and y > -1 and not grid_map[x][y]:
            log("attempt to add cell")
            bp_glyph.add_point(x*10,y*10,cell_ring)
            #show_object(cell_ring.translate((x*10,y*10,5)))
            grid_map[x][y] = True
            
        else:
            log("change direction")
            x = old_x
            y = old_y
            cell_count = old_cell_count
            
            new_dir_index = directions.index(dir)+1
            
            if new_dir_index < len(directions):
                dir = directions[new_dir_index]
                log(f"new dir {dir=}")
            else:
                dir = directions[0]
        
        #if 
        create_points_three(bp_glyph, grid_map,cell_count,x,y,dir)
    else:
        log("end loop")

#-----------

log("#------------")
log("start run")
log("#------------")

grid_map = make_collision_map()
for i,row in enumerate(grid_map):
    log(f"row {i} {row}")

bp_glyph = CircuitGlyph()
cell_ring = ring(4,2,3)
#bp_glyph.add_point(-10,0,cell_ring)

create_points_three(bp_glyph, grid_map, 25, 1)

bp_glyph.make()

ex_glyph = bp_glyph.build()

#show_object(ex_glyph)

cq.exporters.export(ex_glyph,'stl/greeble_circuit_maze.stl')
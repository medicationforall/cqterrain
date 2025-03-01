import random
from typing import Tuple

#--------------
# makes the grid mapping what cell is supposed to be what.
def stacked_wave_form_map(
    size:Tuple[int,int]=(10,10),
    seed:str|None = 'test',
    cell_types:list[str] = ['block','block','empty','block']
) -> list[list[str]]:
    #log("run wfc")
    if seed:
        random.seed(seed)
    
    wfc_grid:list[list] = []
    for row in range(size[0]):
        cells:list[str] = []
        for cell in range(size[1]):
            
            if row>0:
                if wfc_grid[row-1][cell] == 'empty':
                    cells.append('empty')
                else:
                    #random cell
                    type = random.choice(cell_types)
                    cells.append(type)
            else:
                #random cell
                type = random.choice(cell_types)
                cells.append(type)
            
        wfc_grid.append(cells)

    return wfc_grid
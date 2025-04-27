import cadquery as cq

def stucco_brick_blocks(
        wfc_data:list[list[str]], 
        length:float = 10, 
        width:float = 5, 
        height:float = 5,
        spacing:float = 2
    ) -> cq.Workplane:
    #log('-------------------')
    #log('make_grid_of_blocks')
    #make block
    block = cq.Workplane("XY").box(length, width, height).tag('keep')
    fill_block = cq.Workplane("XY").box(length+spacing,width+spacing,height)

    y_count:int= len(wfc_data)
    x_count:int = len(wfc_data[0])
    
    count = 0
    row = 0
    
    keep_blocks = cq.Workplane("XY")
    remove_blocks = cq.Workplane("XY")
    
    def add_block(loc:cq.Location)->cq.Shape:
        nonlocal count
        nonlocal row
        nonlocal keep_blocks
        nonlocal remove_blocks
        cell = count % y_count
        
        offset = 0
        if cell % 2 == 0:
            offset = 5

        block_type = wfc_data[cell][row]
            
        #log(f'{count=}, {row=}, {cell=}, {block_type=}')
        if count != 0 and cell == y_count-1:
            #log('increase row')
            row += 1
        count += 1
        
        if block_type is 'block':
            k_block = block.translate((offset,0,0)).val().located(loc) #type:ignore
            keep_blocks = keep_blocks.add(k_block)
            return k_block #type:ignore
        else:
            r_block = fill_block.translate((offset,0,0)).val().located(loc) #type:ignore
            remove_blocks = remove_blocks.add(r_block)
            return r_block #type:ignore
    
    #made grid
    blocks = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = length+spacing, 
            ySpacing = width+spacing,
            xCount = x_count, 
            yCount= y_count, 
            center = True)
        .eachpoint(add_block)
    )
      
    return keep_blocks.union(remove_blocks)
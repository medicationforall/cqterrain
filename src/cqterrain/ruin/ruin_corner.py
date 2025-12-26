import cadquery as cq

def ruin_corner(
        length:float = 50, 
        width:float = 50, 
        height:float = 10, 
        points:int = 7,
        adjustments:list[tuple[float,float]] = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
        debug:bool = False
    ):
    #outline = cq.Workplane("XY").box(length,width,height)
    
    pts:list[tuple[float,float]] = [(0,0)]#,(0,width),(length,0)]
    
    x_step = length / (points+1)
    y_step = width / (points+1)
    
    test_cube = cq.Workplane("XY").box(1,1,1)
    test_cubes = cq.Workplane("XY")
    
    #build out your points
    for i in range(points+2):
        x_translate:float = x_step*i
        y_translate:float = width - (y_step*i)
        
        if i > 0 and i < points+1 and (i-1) < len(adjustments):
            coord = adjustments[i-1]
            x_translate += coord[0]
            y_translate += coord[1]
        
        pts.append((x_translate, y_translate))
        
        test_cubes = (
            test_cubes.add(
                test_cube
                .translate((x_translate,y_translate,0))
            )
        )
        
    ruin = (
        cq.Workplane("XY")
        .polyline(pts)
        .close()
    )

    if height:
        ruin = ruin.extrude(height)
        
    if debug:
        ruin = ruin.add(test_cubes)
    
    return ruin
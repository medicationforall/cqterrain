import cadquery as cq
from numpy import arange
import random
from .. import obelisk

def resolve_range_val(v)->float|int:
    if type(v) == tuple:
        range_values = arange(v[0],v[1]+v[2],v[2])
        v = random.choice(range_values)
        
    return v

def crystal_random(
        height:tuple[float,float,float]|float = (20,70,2.5),#min,max,step
        base_width:tuple[float,float,float]|float = 20.0,
        base_height:tuple[float,float,float]|float = 0.5,
        inset_width:tuple[float,float,float]|float = 25.0,
        inset_height:tuple[float,float,float]|float = 3.1,
        mid_height:tuple[float,float,float]|float = (2.0,10.0,0.5),
        mid_width:tuple[float,float,float]|float = (20,35.0,2.5),
        top_height:tuple[float,float,float]|float = (20,40,5),
        top_width:tuple[float,float,float]|float = (20,35.0,2.5),
        faces:tuple[int,int,int]|int = (4,8,1),#min,max,step
        seed:str|None = "test",
        intersect:bool = True
    ):
    
    if seed:
        random.seed(seed)
        
    height = resolve_range_val(height)
    
    base_width = resolve_range_val(base_width)
    base_height = resolve_range_val(base_height)
    inset_width = resolve_range_val(inset_width)
    inset_height = resolve_range_val(inset_height)
    
    faces = resolve_range_val(faces) #type:ignore
    mid_height = resolve_range_val(mid_height)
    mid_width = resolve_range_val(mid_width)
    top_height = resolve_range_val(top_height)
    top_width = resolve_range_val(top_width)
    
    crystal = obelisk(
            base_width = base_width,
            base_height = base_height,
            inset_width = inset_width,
            inset_height = inset_height,
            mid_width = mid_width,
            mid_height = mid_height,
            top_width = top_width,
            top_height = top_height,
            height = height,
            faces = faces, #type:ignore
            intersect = intersect
        )#.rotate((0,0,1),(0,0,0),0)
    
    return crystal,height
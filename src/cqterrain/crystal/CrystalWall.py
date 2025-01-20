import cadquery as cq
from cadqueryhelper import Base
from cqterrain.minibase import slot_uneven
from cqterrain.crystal import crystal_random
import random
from numpy import arange

def resolve_range_val(v)->float|int:
    if type(v) == tuple:
        range_values = arange(v[0],v[1]+v[2],v[2])
        v = random.choice(range_values)
        
    return v

class CrystalWall(Base):
    def __init__(self):
        super().__init__()
        
        #parameters
        self.length:float = 75
        self.width:float = 25
        self.height:float = 30
        
        self.render_base:bool = True
        self.seed:str = 'test'
        self.base_height:float = 3
        self.min_height:float = 20
        self.crystal_count:int = 5
        self.crystal_margin:float = 10
        self.random_rotate_x:tuple[float,float,float]|float|None = (-20.0, 20.0, 2.5)
        self.random_rotate_y:tuple[float,float,float]|float|None = (-15.0, 15.0, 2.5)
        
        #shapes
        self.crystals = None
        self.mini_base = None
        self.base_cut = None
        
    def make_mini_base(self):
        self.mini_base = slot_uneven(
            length = self.length,
            width = self.width,
            base_height = self.base_height,
            seed = self.seed
        )
        
    def crystal_adder(self):
        # closure
        count = 0
        def add_crystal(loc:cq.Location)->cq.Shape:
            nonlocal count
            count += 1
            adder_seed = f"{self.seed}_{count}"
            #log(f'{adder_seed}')
            crystal,height = crystal_random(
                height = (self.min_height,self.height,2.5),
                seed = adder_seed,
                
                base_width = 20.0,
                base_height = 0.5,
                inset_width = 20.0,
                inset_height = (1.0,3.0,0.5),
                mid_height = (2.0,5.0,0.5),
                mid_width = (10,20.0,2.5),
                top_height = (10,15,2.5),
                top_width = (10,15.0,2.5),
                faces=(5,10,1),#min,max,step
                intersect = True
            )
            crystal = crystal.translate((0,0,height/2))
            
            if self.random_rotate_x:
                random_rotate_x = resolve_range_val(self.random_rotate_x)
                #log(f'{random_rotate_x}')
                crystal = crystal.rotate((1,0,0),(0,0,0),random_rotate_x)
                
            if self.random_rotate_y:
                random_rotate_y = resolve_range_val(self.random_rotate_y)
                #log(f'{random_rotate_y}')
                crystal = crystal.rotate((0,1,0),(0,0,0),random_rotate_y)
                
            
            return crystal.val().located(loc) #type:ignore
        return add_crystal
        
    def make_crystals(self):
        x_spacing = (self.length - self.crystal_margin * 2) / self.crystal_count
        group = (
            cq.Workplane("XY")
            .rarray(
            xSpacing = x_spacing, 
            ySpacing = self.width,
            xCount = self.crystal_count, 
            yCount= 1,
            center = True)
            .eachpoint(callback = self.crystal_adder())
        )
        
        self.crystals = group
        
    def make_base_cut(self):
        self.base_cut = (
            cq.Workplane("XY").box(
                self.length,
                self.width,
                self.height
            )
        )
    
    def make(self, parent=None):
        super().make(parent)
        
        self.make_crystals()
        
        if self.render_base:
            self.make_mini_base()
            
        self.make_base_cut()
        
    def build(self):
        super().build()
        scene = cq.Workplane("XY")#.box(10,10,10)
        
        if self.crystals:
            scene = scene.union(self.crystals)
        
        if self.render_base and self.mini_base:
            scene = scene.union(self.mini_base.translate((0,0,self.base_height/2)))
            
        if self.base_cut:
            scene= scene.cut(self.base_cut.translate((0,0,-self.height/2)))
            
        return scene
import cadquery as cq
from cadqueryhelper.shape import teardrop
from . import SwivelTop


class Turbine(SwivelTop):
    def __init__(self):
        super().__init__()
        #parameters
        self.mast_height:float = 35
        self.mast_diameter:float = 5
        
        self.cap_diameter:float = 6
        self.cap_height:float = 4
        
        self.blade_count:int = 3
        self.blade_length:float = 10
        self.blade_width:float = 3
        self.blade_rotate:float = (90+45)
        self.blade_radius:float = 12
        self.blade_offset:float = 0
        
        self.fin_count:int = 6
        
        #shapes
        self.mast = None
        self.cap = None
        self.blade = None
        self.blades = None
        self.connector = None
        self.fins = None
        
    def make_mast(self):
        mast = cq.Workplane("XY").cylinder(
            self.mast_height, 
            self.mast_diameter/2
        )
        
        self.mast = mast
        
    def make_cap(self):
        cap = cq.Workplane("XY").cylinder(
            self.cap_height, 
            self.cap_diameter/2
        )
        
        self.cap = cap
        
    def make_blade(self):
        #blade = (
        #    cq.Workplane("XY")
        #    .center(self.blade_radius,0)
        #    .rect(2,self.blade_width)
        #    .center(-self.blade_radius,0)
        #).twistExtrude(self.mast_height,self.blade_rotate)
        
        blade_sketch = teardrop(
            diameter = self.blade_width,
            length= self.blade_length,
            height = 0
        )
        
        blade = (
            cq.Workplane("XY")
            .pushPoints([(-self.blade_radius,-self.blade_width/2)])
            .placeSketch(blade_sketch)
            #.toPending()
            #.center(-10,0)
            
        ).twistExtrude(self.mast_height,self.blade_rotate)
        
        #show_object(blade)
        self.blade = blade
        
    def make_blades(self):
        blades = cq.Workplane("XY")
        
        if self.blade:
            
            rotate_deg = 360 / self.blade_count
            
            for i in range(self.blade_count):
                blades = blades.add(self.blade.rotate((0,0,1),(0,0,0),rotate_deg*i))
            
        self.blades = blades
        
    def make_connector(self):
        length = self.blade_radius+1
        connector = (
            cq.Workplane("XY")
            .box(length,2,2)
            .translate((-(length/2),0,0))
        )
        
        rotate_deg = 360 / self.blade_count
        spokes = cq.Workplane("XY")
        
        for i in range(self.blade_count):
            spokes = spokes.add(
                connector
                .rotate((0,0,1),(0,0,0),rotate_deg*i)
            )
            
            
        rotor = cq.Workplane("XY").cylinder(1.5, self.cap_diameter/2)
        
        self.connector = spokes.union(rotor)
        
    def make_fins(self):
        fin = (
            cq.Workplane("XY")
            .box(5,2,4)
            .faces("Z").edges(">X").chamfer(2)
            .translate((self.mast_diameter/2 + 4/2,0,4/2))
        )
        
        rotate_deg = 360 / self.fin_count
        fins = cq.Workplane("XY")
        
        for i in range(self.fin_count):
            fins.add(fin.rotate((0,0,1),(0,0,0),rotate_deg*i))
        
        self.fins = fins
        
    def make(self):
        super().make()
        self.make_mast()
        self.make_cap()
        self.make_blade()
        self.make_blades()
        self.make_connector()
        self.make_fins()
        
    def build(self)->cq.Workplane:
        #part = cq.Workplane("XY")
        part = super().build()
        
        if self.mast:
            z_translate = self.mast_height/2 + self.height
            part = part.union(self.mast.translate((0,0,z_translate)))
        
        if self.cap:
            z_translate = self.cap_height /2 + self.mast_height + self.height
            part = part.union(self.cap.translate((0,0,z_translate)))
        
        if self.blades:
            z_translate = self.height + self.cap_height + self.blade_offset
            part = part.union(self.blades.translate((0,0,z_translate)))
            
        if self.connector:
            z_translate_bottom = self.height + self.cap_height + self.mast_height/4 + self.blade_offset
            z_translate_top = self.height + self.cap_height + self.mast_height - self.mast_height/4 + self.blade_offset
            rotate_deg = self.blade_rotate/4
            
            part = (
                part
                .union(
                    self.connector
                    .translate((0,0,z_translate_bottom))
                    .rotate((0,0,1),(0,0,0),-rotate_deg)
                )
                .union(
                    self.connector
                    .translate((0,0,z_translate_top))
                    .rotate((0,0,1),(0,0,0),rotate_deg)
                )
            )
            
        if self.fins:
            z_translate = self.height
            part = part.union(self.fins.translate((0,0,z_translate)))
            
        
        return part
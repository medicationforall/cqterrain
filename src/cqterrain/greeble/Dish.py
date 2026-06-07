import cadquery as cq
from cadqueryhelper import Base

class Dish(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 40
        self.width:float = 23
        self.height:float = 2
        self.short_length:float|None = None
        self.rotate:float = 0
        self.diameter:float = self.width+5
        self.outer_diameter:float = 70

        self.render_connector:bool = True
        self.connector_diameter:float = 5
        self.connector_length:float = 2
        self.connector_cylinder_diameter:float = 3
        self.connector_cylinder_length:float = 4
        self.connector_height:float = 4

        self.dish_render:bool = True
        self.dish_z_translate:float = 0.2
        
        self.render_mount:bool = True
        self.mount_length:float = 6

        self.render_collector:bool = True
        self.collector_horn_height:float = 5
        self.collector_horn_diameter:float = 4
        self.collector_arm_length:float = 2
        self.collector_arm_width:float = 2
        self.collector_arm_height:float = 14
        self.collector_arm_rotate:float = -37
        self.collector_z_translate:float = 15.9
        
        #shapes
        self.outline:cq.Workplane|None = None
        self.dish:cq.Workplane|None = None
        self.connector:cq.Workplane|None = None
        self.mount:cq.Workplane|None = None
        self.collector:cq.Workplane|None = None
        
    def calculate_short_length(self)->float:
        if self.short_length:
            return self.short_length
        else:
            return self.diameter if self.diameter < self.length else self.length
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_dish(self):
        flat = cq.Workplane("XY").rect(self.length,self.width).extrude(self.length)
        circle = cq.Workplane("XY").circle(self.diameter/2).extrude(self.length)
        
        short_length =  self.calculate_short_length()
        
        short = cq.Workplane("XY").rect(short_length,self.width).extrude(self.length)
        
        x_translate = self.length/2 - self.diameter/2
        outline = (
            cq.Workplane("XY")
            .union(circle.translate((x_translate,0,0)))
            .union(circle.translate((-x_translate,0,0)))
            .intersect(flat)
            .add(short)
        ).translate((0,0,-self.length/2))
        
        circle_height = self.width+7
        circle = (
            cq.Workplane("XZ")
            .cylinder(circle_height, self.outer_diameter/2)
            .faces("|Y")
            .fillet((circle_height/2)-.00001)
        )
        
        z_translate = self.outer_diameter/2 - self.length/2 
        
        test = (
            cq.Workplane("XY")
            .union(outline)
            .intersect(circle.translate((0,0,z_translate)))
            #.intersect(outline.rotate((0,1,0),(0,0,0),90))
        )
        
        self.flat = test
        
        z_translate = 0#bp_test.bp_base.height + self.width/2
        #rotate_deg = 45
        test_2 = (
            cq.Workplane("XY")
            .union(test)
            .cut(test.translate((0,0,self.height)))
        )
        
        self.dish = test_2.translate((0,0,self.length/2))
        
    def make_connector(self):
        length = self.connector_length
        diameter = self.connector_diameter
        cylinder_diameter = self.connector_cylinder_diameter
        cylinder_length = self.connector_cylinder_length
        rectangle_height = self.connector_height

        connector = cq.Workplane("YZ").cylinder(length, diameter/2)
        cylinder = cq.Workplane("YZ").cylinder(cylinder_length, cylinder_diameter/2)
        rectangle = cq.Workplane("XY").box(length, diameter, rectangle_height)
        
        self.connector = (
            connector
            .union(cylinder)
            .union(rectangle.translate((0,0,rectangle_height/2)))
            
        ).translate((0,0,-diameter/2))
        
    def make_mount(self):
        diameter = self.connector_diameter + 0.2
        mount = cq.Workplane("XY").box(self.mount_length, diameter, self.width/2)
        connector = cq.Workplane("YZ").cylinder(self.mount_length, diameter/2)

        length = self.connector_length + 0.2
        
        cylinder_length = self.connector_cylinder_length + 0.4
        cylinder_diameter = self.connector_cylinder_diameter + 0.4
        
        z_translate = self.width/4
        cut_mount = cq.Workplane("XY").box(length,diameter,diameter)
        cut_cylinder = cq.Workplane("YZ").cylinder(cylinder_length, cylinder_diameter/2)
        
        cut_connector = (
            cut_mount
            .union(cut_cylinder)
            .translate((0,0,z_translate))
        )
        
        mount = mount.union(connector.translate((0,0,self.width/4)))
        
        self.mount = mount.cut(cut_connector)
        
    def make_collector(self):
        height = self.collector_horn_height
        diameter = self.collector_horn_diameter

        length = self.collector_arm_length
        width = self.collector_arm_width
        arm_height = self.collector_arm_height
        arm_rotate = self.collector_arm_rotate

        cylinder = cq.Workplane("XY").cylinder(height,diameter/2)
        connector = cq.Workplane("XY").box(length, width, arm_height)
        
        combined = (
            cylinder
            .add(connector.translate((0,diameter/4,-arm_height/2)).rotate((1,0,0),(0,0,0), arm_rotate))
            
            #.translate((0,0,35))
            #add(connector.translate((0,4/4,-14/2)).rotate((1,0,0),(0,0,0),-37).rotate((0,0,1),(0,0,0),180))
            #.add(connector.translate((0,4/4,-14/2)).rotate((1,0,0),(0,0,0),-37).rotate((0,0,1),(0,0,0),90))
        )
        
        self.collector = combined
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_dish()
        self.make_connector()
        self.make_mount()
        self.make_collector()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.dish and self.dish_render:
            z_translate = self.dish_z_translate
            part = part.union(self.dish.translate((0,0,z_translate)))
        
        if self.collector and self.render_collector:
            z_translate = self.collector_z_translate
            part = part.add(self.collector.translate((0,0,z_translate)))

        if self.connector and self.render_connector:
            z_translate = 0
            part = part.union(self.connector.translate((0,0,z_translate)))
        
        #rotate transform
        z_translate = self.width/2
        part = (
            part
            .translate((0,0,self.connector_diameter/2))
            .rotate((1,0,0),(0,0,0),self.rotate)
            .translate((0,0,(z_translate)))
        )
        
        if self.mount and self.render_mount:
            z_translate = self.width /4
            part = part.add(self.mount.translate((0,0,z_translate)))
            
        return part
import cadquery as cq
from cadqueryhelper import Base, shape
from cqterrain import tile

class TilesPlate(Base):
    def __init__(self):
        super().__init__()
        
        # shapes
        self.tiles = []
        
    def __make_tiles(self):
    
        apricorn = tile.apricorn(
            length = 30, 
            width = 25, 
            height = 4,
            line_width = 2,
            line_depth = .5,
            center_radius = None,
            width_radius_divisor = 4
        )
        self.tiles.append(apricorn)
        
        
        basketweave = tile.basketweave(
            length = 14,
            width = 7,
            height = 2,
            padding = .5
        )
        self.tiles.append(basketweave)
        
        bolt_panel = tile.bolt_panel(
            length = 30, 
            width = 30, 
            height = 3, 
            chamfer = .5, 
            radius_outer=2,
            radius_internal=1,
            cut_height=0.5,
            padding = 4
        )
        self.tiles.append(bolt_panel)
        
        carton = tile.carton(
            length=30, 
            width=30, 
            height = 4,
            line_width = 3,
            line_depth = 1.5,
            x_divisor = 3,
            y_divisor = 2
        )
        self.tiles.append(carton)
        
        carton2 = tile.carton2(
            length = 30, 
            width = 25, 
            height = 4, 
            line_width = 2, 
            line_depth = 1.5,
            x_divisor = 2,
            y_divisor = 3
        )
        self.tiles.append(carton2)
        
        #----------------
        
        chamfer_frame = tile.chamfer_frame(
            length = 25,
            width = 25,
            height = 4,
            chamfer_length = 8,
            padding = .5,
            frame_width = 3,
            internal_height_cut = 2
        )
        self.tiles.append(chamfer_frame)
        
        charge = tile.charge(
            length = 30, 
            width = 25, 
            height = 4,
            line_width = 3,
            line_depth = 1,
            corner_chamfer = 4,
            edge_chamfer = 2,
            padding = 2.5
        )
        self.tiles.append(charge)
        
        conduit = tile.conduit(
            length = 30,
            width = 25,
            height = 4,
            frame= 1,
            frame_depth =3,
            pipe_count = None,
            radius = 4,
            inner_radius = 3,
            segment_length = 6,
            space = 4,
            pipe_padding = 1
        )
        self.tiles.append(conduit)
        
        
        glyph = tile.glyph(
            length = 14,
            width = 7,
            height = 2,
            padding = .5
        )
        self.tiles.append(glyph)
        
        
        octagon_with_dots_2 = tile.octagon_with_dots_2(
            tile_size = 25,
            chamfer_size = 7.5,
            mid_tile_size = 8,
            spacing = 2,
            tile_height = 2.5
        )
        self.tiles.append(octagon_with_dots_2)
        
        
        #----------------
        
        plain = tile.plain(
            length = 25,
            width = 25,
            height = 2,
            padding = 1
        )
        self.tiles.append(plain)
        
        
        rivet = tile.rivet(
            length = 25,
            width = 25,
            height = 2,
            padding = 1,
            internal_padding = 8,
            rivet_height = 1,
            rivet_radius = 1.5
        )
        self.tiles.append(rivet)
        
        
        rivet_round = tile.rivet_round(
            radius = 12.5, 
            height = 3,
            rivet_height = 0.5,
            rivet_radius = 1.5,
            padding = 1.5,
            rivet_count = 5
        )
        self.tiles.append(rivet_round)
        
        
        slot_diagonal = tile.slot_diagonal(
            tile_size = 21,
            height = 2,
            slot_width = 2,
            slot_height = 2,
            slot_length_padding = 7,
            slot_width_padding = 2,
            slot_width_padding_modifier = .25
        )
        self.tiles.append(slot_diagonal)
        
        
        slot = tile.slot(
            length = 25,
            width = 23,
            height = 3,
            padding = 2,
            slot_length_padding = 5,
            slot_width_offset = 3,
            slot_width = 3,
            slot_height = 0.5
        )
        self.tiles.append(slot)
        
        #----------------
        
        truchet_circle = tile.truchet_circle(
            length = 25,
            width = 25,
            height = 4,
            radius = 3, 
            base_height = 2,
            shift_design=6
        )
        self.tiles.append(truchet_circle)
        
        

        truchet_triangle = tile.truchet_triangle(
            length = 25, 
            width = 25, 
            height = 4, 
            min_height = 2
        )
        self.tiles.append(truchet_triangle)
        
        
        windmill = tile.windmill(
            tile_size = 25,
            height = 3,
            padding = 1.5
        )
        self.tiles.append(windmill)
        
        
        #plain = tile.plain(
        #    length = 25,
        #    width = 25,
        #    height = 2,
        #    padding = 1
        #)
        #self.tiles.append(plain)
        
        
        #plain = tile.plain(
        #    length = 25,
        #    width = 25,
        #    height = 2,
        #    padding = 1
        #)
        #self.tiles.append(plain)
    


        
    def make(self, parent=None):
        super().make(parent)
        self.backdrop = shape.backdrop(length=500)
        self.__make_tiles()

        
    def build(self):
        super().build()
        scene = (
            cq.Workplane("XY")
            .union(self.backdrop.translate((0,0,68)))
        )
        
        shapes = cq.Workplane("XY")
        
        column = -1
        for i,shape in enumerate(self.tiles):
            if i %5 ==0:
                column+=1
            shapes = shapes.union(shape.translate(((column)*50,(i%5)*-40,0)))
        
        return scene.union(shapes.translate((-((3*50)/2),((4*40)/2),0)))
    
    def build_assembly(self):
        shapes = cq.Workplane("XY")
        
        column = -1
        for i,shape in enumerate(self.tiles):
            if i %5 ==0:
                column+=1
            shapes = shapes.union(shape.translate(((column)*50,(i%5)*-40,0)))
        
        assembly = cq.Assembly()
        assembly.add(self.backdrop.translate((0,0,68)), color=cq.Color(1, 1,1 ), name="backdrop")
        assembly.add(shapes.translate((-((3*50)/2),((4*40)/2),0)), color=cq.Color(0, 0, 1), name="shapes")
        return assembly
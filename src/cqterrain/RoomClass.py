import cadquery as cq
from cadqueryhelper import series, shape
from .floor import floor
from .wall import wall


class RoomClass:
    def __init__(self, length=120, width=80, height=50, wall_width=3, floor_height=3, floor_padding=0, window_count=1, style="office"):
        # attributes
        self.length = length
        self.width = width
        self.height = height
        self.wall_width = wall_width
        self.floor_height = floor_height
        self.floor_padding = floor_padding
        self.style = style
        self.window_count = window_count

        # post make
        self.floor = None
        self.walls = []

    def __make_floor(self):
        padding = self.floor_padding*2
        r_floor = floor(self.length, self.width, self.floor_height)
        self.r_height = r_floor.metadata['height']
        self.r_width = r_floor.metadata['width'] - padding
        self.r_length = r_floor.metadata['length'] - padding
        return r_floor

    def __make_wall(self, length, width, height):
        w = wall(length, width, height)
        self.w_height = w.metadata['height']
        self.w_width = w.metadata['width']

        if self.style == "office":
            print('windows style is arch')
            window_cutout = cq.Workplane().box(10, width, 20)
            window_series = series(window_cutout, self.window_count, length_offset = 1)
            w = w.cut(window_series)
        elif self.style == "arch":
            print('windows style is arch')
            window_cutout = shape.arch_pointed(length=10, width=width, height=20, inner_height=10)
            window_series = series(window_cutout, self.window_count, length_offset = 1)

            window_ridge = shape.arch_pointed(length=12, width=width+2, height=22, inner_height=11)
            window_cutout2 = shape.arch_pointed(length=10, width=width+2, height=20, inner_height=10)
            window = window_ridge.cut(window_cutout2)
            window_series2 = series(window, self.window_count, length_offset = 1)
            w = w.cut(window_series).add(window_series2)
        return w

    def make(self):
        # make floor
        r_floor = self.__make_floor()
        self.floor = r_floor

        # make walls along the x axis
        w1  = self.__make_wall(length=self.r_length, width=self.wall_width, height=self.height)
        w2 = self.__make_wall(length=self.r_length, width=self.wall_width, height=self.height)

        # walls along the y axis
        w3 = self.__make_wall(length=self.r_width, width=self.wall_width, height=self.height)
        w3_rotated = w3.rotate((0, 0, 1), (0, 0, 0), -90)

        w4 = self.__make_wall(length=self.r_width, width=self.wall_width, height=self.height)
        w4_rotated = w4.rotate((0, 0, 1), (0, 0, 0), -90)

        self.walls.append(w1)
        self.walls.append(w2)
        self.walls.append(w3_rotated)
        self.walls.append(w4_rotated)

    def build(self):
        room_assembly = cq.Assembly()
        room_assembly.add(self.floor, name="floor")
        room_assembly.add(self.walls[0], name="wall1", loc=cq.Location(cq.Vector(0, (self.r_width /2) - (self.w_width /2), (self.w_height /2)-(self.r_height/2))))
        room_assembly.add(self.walls[1], name="wall2", loc=cq.Location(cq.Vector(0, -1*((self.r_width /2) - (self.w_width /2)), (self.w_height /2)-(self.r_height/2))))
        room_assembly.add(self.walls[2], name="wall3", loc=cq.Location(cq.Vector((self.r_length /2) - (self.w_width /2), 0, (self.w_height /2)-(self.r_height/2))))
        room_assembly.add(self.walls[3], name="wall4", loc=cq.Location(cq.Vector(-1*((self.r_length /2) - (self.w_width /2)), 0, (self.w_height /2)-(self.r_height/2))))
        comp_room = room_assembly.toCompound()

        # zero out height
        comp_room = comp_room.translate((0,0, self.floor_height/2))
        comp_room = comp_room.translate((0,0, -1*(self.height/2)))

        return comp_room

import cadquery as cq
from cadqueryhelper import series, shape
from .floor import floor
from .Wall import Wall
from .Door import Door


class Room:
    def __init__(
    self,
    length=120,
    width=80,
    height=50,
    wall_width=3,
    floor_height=3,
    floor_padding=0,
    window_count=1,
    style="office",
    door_walls = [False, True, False, False],
    window_walls = [True, True, True, True],
    build_walls = [True, True, True, True]
    ):
        # attributes
        self.length = length
        self.width = width
        self.height = height
        self.wall_width = wall_width
        self.floor_height = floor_height
        self.floor_padding = floor_padding
        self.style = style
        self.window_count = window_count
        self.door_walls = door_walls
        self.window_walls = window_walls
        self.build_walls = build_walls

        # post make
        self.floor = None
        self.walls = []
        self.doors = []

        self.door = {}
        self.door['length'] = 25
        self.door['width'] = wall_width+2
        self.door['frame_length'] = 3
        self.door['frame_height'] = 4
        self.door['inner_width'] = 3
        self.door['height'] = height-20
        self.door['x_offset'] = 0



    def __make_floor(self):
        padding = self.floor_padding*2
        r_floor = floor(self.length, self.width, self.floor_height)
        self.r_height = r_floor.metadata['height']
        self.r_width = r_floor.metadata['width'] - padding
        self.r_length = r_floor.metadata['length'] - padding
        return r_floor

    def __make_wall(self, length, width, height, door_wall, window_wall):
        b_wall = Wall(length, width, height)
        b_wall.make()
        w = b_wall.build()
        #print('wall built', dir(w))
        self.w_height = b_wall.height
        self.w_width = b_wall.width


        if self.style == "office" and window_wall:
            window_cutout = cq.Workplane().box(10, width, 20)
            window_series = series(window_cutout, self.window_count, length_offset = 1)
            w = w.cut(window_series)
        elif self.style == "arch" and window_wall:
            window_cutout = shape.arch_pointed(length=12, width=width, height=22, inner_height=10)
            window_series = series(window_cutout, self.window_count, length_offset = 1)

            window_ridge = shape.arch_pointed(length=12, width=width+2, height=22, inner_height=11)
            window_cutout2 = shape.arch_pointed(length=10, width=width+2, height=20, inner_height=10)
            window = window_ridge.cut(window_cutout2)
            window_series2 = series(window, self.window_count, length_offset = 1)
            w = w.cut(window_series).add(window_series2)

        if door_wall:
            #print('attempt to make door')
            #zero wall
            w = w.translate((0,0,height/2))

            # door logic
            door_bb = Door(**self.door)
            door_bb.make()
            door_outline = door_bb.outline.translate((0,0,(door_bb.height/2)+self.floor_height))
            door = door_bb.build().translate((0,0,(door_bb.height/2)+self.floor_height))
            w = w.cut(door_outline).union(door)

            #center all
            w = w.translate((0,0,-1*(height/2)))
        return w

    def make(self):
        # make floor
        r_floor = self.__make_floor()
        self.floor = r_floor

        # make walls along the x axis
        w1  = self.__make_wall(length=self.r_length, width=self.wall_width, height=self.height, door_wall = self.door_walls[0], window_wall = self.window_walls[0])
        w1_rotated = w1.rotate((0, 0, 1), (0, 0, 0), 180)
        w2 = self.__make_wall(length=self.r_length, width=self.wall_width, height=self.height, door_wall = self.door_walls[1],  window_wall = self.window_walls[1])

        # walls along the y axis
        w3 = self.__make_wall(length=self.r_width, width=self.wall_width, height=self.height, door_wall = self.door_walls[2],  window_wall = self.window_walls[2])
        w3_rotated = w3.rotate((0, 0, 1), (0, 0, 0), -90)

        w4 = self.__make_wall(length=self.r_width, width=self.wall_width, height=self.height, door_wall = self.door_walls[3],  window_wall = self.window_walls[3])
        w4_rotated = w4.rotate((0, 0, 1), (0, 0, 0), 90)

        self.walls=[]
        self.walls.append(w1_rotated)
        self.walls.append(w2)
        self.walls.append(w3_rotated)
        self.walls.append(w4_rotated)

    def build(self):
        room_assembly = cq.Assembly()
        room_assembly.add(self.floor, name="floor")
        if self.build_walls[0]:
            room_assembly.add(self.walls[0], name="wall1", loc=cq.Location(cq.Vector(0, (self.r_width /2) - (self.w_width /2), (self.w_height /2)-(self.r_height/2))))

        if self.build_walls[1]:
            room_assembly.add(self.walls[1], name="wall2", loc=cq.Location(cq.Vector(0, -1*((self.r_width /2) - (self.w_width /2)), (self.w_height /2)-(self.r_height/2))))

        if self.build_walls[2]:
            room_assembly.add(self.walls[2], name="wall3", loc=cq.Location(cq.Vector((self.r_length /2) - (self.w_width /2), 0, (self.w_height /2)-(self.r_height/2))))

        if self.build_walls[3]:
            room_assembly.add(self.walls[3], name="wall4", loc=cq.Location(cq.Vector(-1*((self.r_length /2) - (self.w_width /2)), 0, (self.w_height /2)-(self.r_height/2))))
        comp_room = room_assembly.toCompound()

        # zero out height
        comp_room = comp_room.translate((0,0, self.floor_height/2))
        comp_room = comp_room.translate((0,0, -1*(self.height/2)))

        return comp_room

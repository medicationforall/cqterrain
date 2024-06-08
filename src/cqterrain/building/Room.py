# Copyright 2022 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

import cadquery as cq
from cadqueryhelper import series, shape, Base
from typing import Callable
from . import Floor
from . import Wall
from ..door import Door

def _make_custom_windows(wall, length, width, height, count, padding):
    window_cutout = cq.Workplane().box(length, width, height)
    window_series = series(window_cutout, count, length_offset = padding)
    w = wall.cut(window_series)
    return w

def _make_custom_door(wall, length, width, height, floor_height):
    bottom = wall.faces("-Z").val()
    cutout = (cq.Workplane(bottom.Center())
              .box(length, width, height)
              .translate((0,0,(height/2)+floor_height))
              )

    #log(bottom.Center())
    w = wall.cut(cutout)
    return w


class Room(Base):
    '''
    This code is doing too much work. I'm going to refactor this whole concept
    '''
    def __init__(
    self,
    length:float = 120,
    width:float = 80,
    height:float = 50,
    wall_width:float = 3,
    floor_height:float = 3,
    floor_padding:float = 0,

    floor_tile:cq.Workplane|None = None,
    floor_tile_padding:float = 0,
    window_count:int = 1,
    style:str = "office",
    door_walls:list[bool] = [False, True, False, False],
    window_walls:list[bool] = [True, False, True, True],
    build_walls:list[bool] = [True, True, True, True],
    make_custom_windows:Callable[[cq.Workplane, float, float, float, int, float], cq.Workplane]|None = None,
    make_custom_door:Callable[[cq.Workplane, float, float, float, float], cq.Workplane]|None = None
    ):
        # attributes
        self.length:float = length
        self.width:float = width
        self.height:float = height
        self.wall_width:float = wall_width
        self.floor_height:float = floor_height
        self.floor_padding:float = floor_padding
        self.floor_tile:cq.Workplane|None = floor_tile
        self.floor_tile_padding:float = floor_tile_padding
        self.style:str = style
        self.window_count:int = window_count
        self.door_walls:list[bool] = door_walls
        self.window_walls:list[bool] = window_walls
        self.build_walls:list[bool] = build_walls

        # post make
        self.floor:Base|None = None
        self.walls:list[cq.Workplane] = []
        self.doors:list[cq.Workplane] = []

        self.window = {}
        self.window['padding'] = 1
        self.window['length'] = 10
        self.window['height'] = 20

        self.door = {}
        self.door['length'] = 25
        self.door['width'] = wall_width+2
        self.door['frame_length'] = 3
        self.door['frame_height'] = 4
        self.door['inner_width'] = 3
        self.door['height'] = height-20
        self.door['x_offset'] = 0

        # callback
        self.make_custom_windows = make_custom_windows
        self.make_custom_door = make_custom_door


    def __make_floor(self):
        padding = self.floor_padding*2
        floor_bp = Floor(self.length, self.width, self.floor_height, self.floor_tile, self.floor_tile_padding)
        self.r_height = floor_bp.height
        self.r_width = floor_bp.width - padding
        self.r_length = floor_bp.length - padding
        floor_bp.make()
        return floor_bp

    def __make_wall(
            self, 
            length:float, 
            width:float, 
            height:float, 
            door_wall:bool, 
            window_wall:bool
        ):
        # this method is doing too much work
        # I don't like this, I want the blueprints to be parameters.
        bp_wall:Base = Wall(length, width, height)
        bp_wall.make()
        wall:cq.Workplane = bp_wall.build()
        self.w_height = bp_wall.height
        self.w_width = bp_wall.width

        if self.make_custom_windows != None and window_wall:
            wall = self.make_custom_windows(
                wall, 
                self.window['length'], 
                width, 
                self.window['height'], 
                self.window_count, 
                self.window['padding']
            )
        elif self.style == "office" and window_wall:
            wall = _make_custom_windows(wall, self.window['length'], width, self.window['height'], self.window_count, self.window['padding'])
        elif self.style == "arch" and window_wall:
            window_cutout = shape.arch_pointed(length=12, width=width, height=22, inner_height=10)
            window_series = series(window_cutout, self.window_count, length_offset = self.window['padding'])

            window_ridge = shape.arch_pointed(length=12, width=width+2, height=22, inner_height=11)
            window_cutout2 = shape.arch_pointed(length=10, width=width+2, height=20, inner_height=10)
            window = window_ridge.cut(window_cutout2)
            window_series2 = series(window, self.window_count, length_offset = self.window['padding'])
            wall = wall.cut(window_series).add(window_series2)

        if door_wall and self.make_custom_door:
            wall = self.make_custom_door(wall, self.door['length'], self.door['width'], self.door['height'], self.floor_height)
        elif door_wall:
            #print('attempt to make door')
            #zero wall
            wall = wall.translate((0,0,height/2))

            # door logic
            bp_door = Door(**self.door)
            bp_door.make()
            door_outline = bp_door.outline.translate((0,0,(bp_door.height/2)+self.floor_height)) #type: ignore
            door = bp_door.build().translate((0,0,(bp_door.height/2)+self.floor_height))
            wall = wall.cut(door_outline).union(door)

            #center all
            wall = wall.translate((0,0,-1*(height/2)))
        return wall

    def make(self, parent = None):
        super().make(parent)

        # make floor
        self.floor = self.__make_floor()

        # this code shouldn't be doing the rotations for placement, that's a build problem
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

    def build(self) -> cq.Workplane:
        super().build()
        scene = cq.Workplane("XY")

        if self.floor:
            floor = self.floor.build()
            scene = scene.union(floor)
            
        if self.build_walls[0]:
            scene = scene.union(self.walls[0].translate((
                0, 
                (self.r_width /2) - (self.w_width /2), 
                (self.w_height /2)-(self.r_height/2)))
            )

        if self.build_walls[1]:
            scene = scene.union(self.walls[1].translate((
                0, 
                -1*((self.r_width /2) - (self.w_width /2)), 
                (self.w_height /2)-(self.r_height/2)))
            )

        if self.build_walls[2]:
            scene = scene.union(self.walls[2].translate((
                (self.r_length /2) - (self.w_width /2), 
                0, 
                (self.w_height /2)-(self.r_height/2)))
            )

        if self.build_walls[3]:
            scene = scene.union(self.walls[3].translate((
                -1*((self.r_length /2) - (self.w_width /2)), 
                0, 
                (self.w_height /2)-(self.r_height/2)))
            )

        # zero out height
        scene = scene.translate((0,0, self.floor_height/2))
        scene = scene.translate((0,0, -1*(self.height/2)))

        return scene
    

    def build_assembly(self) -> cq.Assembly:
        room_assembly = cq.Assembly()

        if self.floor:
            floor = self.floor.build()
            room_assembly.add(floor, name="floor")
            
        if self.build_walls[0]:
            room_assembly.add(self.walls[0], name="wall1", loc=cq.Location(cq.Vector(0, (self.r_width /2) - (self.w_width /2), (self.w_height /2)-(self.r_height/2))))

        if self.build_walls[1]:
            room_assembly.add(self.walls[1], name="wall2", loc=cq.Location(cq.Vector(0, -1*((self.r_width /2) - (self.w_width /2)), (self.w_height /2)-(self.r_height/2))))

        if self.build_walls[2]:
            room_assembly.add(self.walls[2], name="wall3", loc=cq.Location(cq.Vector((self.r_length /2) - (self.w_width /2), 0, (self.w_height /2)-(self.r_height/2))))

        if self.build_walls[3]:
            room_assembly.add(self.walls[3], name="wall4", loc=cq.Location(cq.Vector(-1*((self.r_length /2) - (self.w_width /2)), 0, (self.w_height /2)-(self.r_height/2))))

        return room_assembly

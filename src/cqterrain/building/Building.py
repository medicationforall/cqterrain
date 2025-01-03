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
# limitations under the License.

import cadquery as cq
from cadqueryhelper import Base
from ..stairs import stairs
from . import Room

class Building(Base):
    def __init__(
        self,
        length:float = 100,
        width:float = 100,
        height:float = 300,
        stories:int = 3,
        has_stairs:bool = False
    ):
        # properties
        self.length:float = length
        self.width:float = width
        self.height:float = height
        self._stories:int = stories
        self._room_height:float = height/stories

        self.floors:list[Base] = []
        self.staircase:list[cq.Workplane] = []

        #make room properties
        self.room = {}
        self.room['length'] = self.length
        self.room['width'] = self.width
        self.room['height'] = self._room_height
        self.room['wall_width'] = 3
        self.room['floor_height'] = 3
        self.room['floor_padding'] = 0
        self.room['floor_tile'] = None
        self.room['floor_tile_padding'] = 0
        self.room['style'] = "office"
        self.room['door_walls'] = [False,False,False,False]
        self.room['window_walls'] = [True,True,True,True]
        self.room['build_walls'] = [True, True, True, True]
        self.room['make_custom_windows'] = None
        self.room['make_custom_door'] = None

        self.window = {}
        self.window['count'] = 1
        self.window['padding'] = 1
        self.window['length'] = 10
        self.window['height'] = 20

        self.door = {}
        self.door ['length'] = 25
        self.door ['height'] = self._room_height - 20

        self.has_stairs = has_stairs
        self.stair_type = 'wrap_exterior'
        self.stair_stories = stories -1

        #make stair properties
        self.stair = {}
        self.stair['rail_height'] = 5
        self.stair['width'] = 10
        self.stair['run'] = 5
        self.stair['length_padding'] = 0
        self.stair['stair_length_offset'] = 0
        self.stair['stair_height'] = 1
        self.stair['stair_height_offset'] = 0
        self.stair['rail_width'] = 1
        self.stair['step_overlap']=None
        self.stair['start_rotation']=0
        self.stair['direction']='counter-clockwise'

        self.stair_landing = {}
        self.stair_landing['width'] = None
        self.stair_landing['length'] = None
        self.stair_landing['height'] = 5

    @property
    def stories(self):
        return self._stories

    @stories.setter
    def stories(self, value):
        self._stories = value
        self._room_height = self.height/self._stories


    def make(self, parent = None):
        super().make(parent)
        self.make_stories()

        if self.has_stairs:
            self.make_stairs()

    def make_stories(self):
        self.floors = []
        for i in range(self._stories):
            floor = Room(**self.room)
            floor.window_count = self.window['count']
            floor.window['padding'] = self.window['padding']
            floor.window['length'] = self.window['length']
            floor.window['height'] = self.window['height']

            floor.door['length'] = self.door['length']
            floor.door['height'] = self.door['height'] 

            floor.make()
            self.floors.append(floor)

    def make_stairs(self):
        stair_map = {
            'wrap_exterior':self.__make_wrap_exterior_stairs
        }

        if self.stair_type in stair_map:
            stair_map[self.stair_type]()
        else:
            raise Exception('I don\'t recognize this stair type')

    def __make_wrap_exterior_stairs(self):
        #print('__make_wrap_exterior_stairs')
        self.stairs = []
        for i in range(self.stair_stories):
            stair_height = self._room_height
            stair_height += self.stair['rail_height']

            if i % 2 == 0:
                stair_length = self.length
                y_offset = self.width
            else:
                stair_length = self.width
                y_offset = self.length

            if i+1==self._stories:
                # todo will need furthe refinement
                stair_height = self._room_height
                stair_height += (self.stair['rail_height']/2)
                z_offset = (i*self._room_height)+self.stair['rail_height']/4
            else:
                z_offset = (i*self._room_height)+self.stair['rail_height']/2

            stair = stairs(
                length = stair_length - self.stair['length_padding'],
                width = self.stair['width'],
                height = stair_height,
                run = self.stair['run'],
                stair_length_offset = self.stair['stair_length_offset'],
                stair_height = self.stair['stair_height'],
                stair_height_offset = self.stair['stair_height_offset'],
                rail_width = self.stair['rail_width'],
                rail_height = self.stair['rail_height'],
                step_overlap = self.stair['step_overlap']
            )

            if self.stair_landing['length'] and self.stair_landing['width']:
                landing = cq.Workplane("XY").box(self.stair_landing['length'], self.stair_landing['width'], self.stair_landing['height'])
                landing = landing.translate(((self.stair_landing['length']/2)+((stair_length - self.stair['length_padding'])/2),0,(stair_height/2)-(self.stair_landing['height']/2)))
                stair = cq.Workplane("XY").add(stair).add(landing)

            if self.stair['direction'] == 'counter-clockwise':
                stair = stair.translate((0, (y_offset/2) + (self.stair['width']/2), z_offset))
                stair  = stair.rotate((0, 0, 1), (0, 0, 0), 90*i).rotate((0, 0, 1), (0, 0, 0), self.stair['start_rotation'])
            elif self.stair['direction'] == 'clockwise':
                stair = stair.rotate((0, 0, 1), (0, 0, 0), 180).translate((0, (y_offset/2) + (self.stair['width']/2), z_offset))
                stair  = stair.rotate((0, 0, 1), (0, 0, 0), -90*i).rotate((0, 0, 1), (0, 0, 0), self.stair['start_rotation'])
            else:
                raise Exception(f"unrecognized stair dirsction {self.stair['direction']}")
            self.stairs.append(stair)


    def build(self) -> cq.Workplane:
        super().build()
        scene = cq.Workplane("XY")

        for i, floor in enumerate(self.floors):
            scene = scene.union(floor.build().translate((0, 0, i*self._room_height))) #type: ignore

        if self.has_stairs:
            for i, stair_case in enumerate(self.stairs):
                scene = scene.union(stair_case.translate((0,0,0)))

        return scene
    
    def build_assembly(self) -> cq.Assembly:
        super().build()
        building_assembly = cq.Assembly()

        # could be a series
        for i, floor in enumerate(self.floors):
            building_assembly.add(floor.build(), name=f"story{i}", loc=cq.Location(cq.Vector(0, 0, i*self._room_height)))

        if self.has_stairs:
            for i, stair_case in enumerate(self.stairs):
                building_assembly.add(stair_case, name=f"stair{i}", loc=cq.Location(cq.Vector(0, 0, 0)))

        return building_assembly

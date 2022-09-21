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
from cadqueryhelper import shape
from .stairs import stairs
from .Room import Room

class Building:
    def __init__(
        self,
        length=100,
        width=100,
        height=300,
        stories=3,
        has_stairs=False
    ):
        # properties
        self.length = length
        self.width = width
        self.height = height
        self._stories = stories
        self._room_height = height/stories

        self.floors = [],
        self.staircase = []

        #make room properties
        self.room = {}
        self.room['length'] = self.length
        self.room['width'] = self.width
        self.room['height'] = self._room_height
        self.room['wall_width'] = 3
        self.room['floor_height'] = 3
        self.room['floor_padding'] = 0
        self.room['style'] = "office"
        self.room['window_count'] = 1
        self.room['style'] = "office"
        self.room['door_walls'] = [False,False,False,False]
        self.room['window_walls'] = [True,True,True,True]
        self.room['build_walls'] = [True, True, True, True]

        self.has_stairs = has_stairs
        self.stair_type = 'wrap_exterior'
        self.stair_stories = stories -1

        #make stair properties
        self.stair = {}
        self.stair['rail_height'] = 5
        self.stair['width'] = 10
        self.stair['run'] = 5
        self.stair['stair_length_offset'] = 0
        self.stair['stair_height'] = 1
        self.stair['stair_height_offset'] = 0
        self.stair['rail_width'] = 1
        self.stair['step_overlap']=None

    @property
    def stories(self):
        return self._stories

    @stories.setter
    def stories(self, value):
        self._stories = value
        self._room_height = self.height/self._stories


    def make(self):
        self.make_stories()

        if self.has_stairs:
            self.make_stairs()

    def make_stories(self):
        self.floors = []
        for i in range(self._stories):
            floor = Room(**self.room)

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
                length = stair_length,
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

            stair_case_width = stair.metadata['width']

            stair = stair.translate((0, (y_offset/2) + (stair_case_width/2), z_offset))
            stair  = stair.rotate((0, 0, 1), (0, 0, 0), 90*i)
            self.stairs.append(stair)


    def build(self):
        '''
        lifecycle
        '''
        building_assembly = cq.Assembly()

        # could be a series
        for i, floor in enumerate(self.floors):
            building_assembly.add(floor.build(), name=f"story{i}", loc=cq.Location(cq.Vector(0, 0, i*self._room_height)))

        if self.has_stairs:
            for i, stair_case in enumerate(self.stairs):
                building_assembly.add(stair_case, name=f"stair{i}", loc=cq.Location(cq.Vector(0, 0, 0)))

        comp_building = building_assembly.toCompound()
        return comp_building#, building_assembly

# Copyright 2024 James Adams
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

class BaseShape(Base):
    '''
    Psuedo Interface defines the minimal properties available for anything that inherits off of BaseShape.
    '''

    def __init__(self):
        super().__init__()
        
        #properties
        self.length:float = 25
        self.width:float = 20
        self.base_height:float = 5
        self.middle_width_inset:float = -6
        
        #shapes
        self.shape:cq.Workplane|None = None

    def build(self) -> cq.Workplane:
        super().build()
        if self.shape:
            return self.shape
        else:
            raise Exception('unable to resolve BaseShape shape')
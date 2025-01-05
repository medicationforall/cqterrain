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
from . import BaseShape, BaseMesh, BaseMagnets, BaseCut

class BaseWall(Base):
    '''
    Psuedo Interface defines the minimal properties available for anything that inherits off of BaseStraight.
    '''

    def __init__(self):
        super().__init__()
        #properties
        self.length:float = 75
        self.height:float = 25
        self.width:float = 20
        self.height:float = 25

        self.base_height:float = 5.6
        self.magnet_padding_x:float = 2
        self.mesh_width: float = 6
        self.render_greeble: bool = True

        #blueprints
        self.shape_bp:BaseShape = BaseShape()
        self.mesh_bp:BaseMesh = BaseMesh()
        self.magnets_bp:BaseMagnets = BaseMagnets()
        self.base_cut_bp:BaseCut = BaseCut()
        

    def build(self) -> cq.Workplane:
        super().build()
        scene = (
            cq.Workplane("XY")
        )
        return scene
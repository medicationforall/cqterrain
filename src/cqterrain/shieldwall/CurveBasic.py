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
from . import ShieldShape, Magnets, BaseMagnets, BaseShape

class CurveBasic(Base):
    def __init__(self):
        super().__init__()
        # properties
        self.width:float = 20
        self.height:float = 25
        self.base_height:float = 5.6
        
        self.x_radius:float = 75
        self.y_radius:float = 75 #ellipse stretch
        self.angle:float = 270
        self.rotation_angle:float = 0
        
        self.render_magnets:bool = True
        self.magnet_padding:float = 1
        self.magnet_padding_x:float = 2
        
        # blueprints
        self.shape_bp:BaseShape = ShieldShape()
        self.magnets_bp:BaseMagnets = Magnets()
        
        #shape
        self.wall:cq.Workplane|None = None
        
    def __make_shape(self, parent=None):
        self.shape_bp.length = self.height
        self.shape_bp.width = self.width
        self.shape_bp.base_height = self.base_height
        self.shape_bp.make(parent)
        
    def __make_magnets(self):
        self.magnets_bp.distance = self.width - self.magnets_bp.pip_radius*2 - self.magnet_padding*2 - self.magnet_padding_x
        self.magnets_bp.make()
        
    def __make_wall(self):
        path = (
            cq.Workplane("ZY")
            .ellipseArc(
                self.x_radius,
                self.y_radius,
                self.angle,
                rotation_angle=self.rotation_angle
            )
        )
        
        self.wall = (
            self.shape_bp.build()
            .sweep(path)
            .rotate((0,1,0),(0,0,0),90)
            .translate((0,-1*(self.y_radius),0))
        )
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_shape()
        self.__make_magnets()
        self.__make_wall()
        
    def build(self) -> cq.Workplane:
        super().build()
        magnets = self.magnets_bp.build()
        
        scene = (
            cq.Workplane("XY")
            .union(self.wall)
        )
        
        if self.render_magnets:
            # note positioning the magnets does not take into account self.rotation_angle
            # if that attribute is reinstated it will have to be adressed here as well
            pip_half_height =  self.magnets_bp.pip_height/2
            magnet_y = self.y_radius
            magnet_z = -(self.height/2) + self.base_height - self.magnets_bp.pip_radius - self.magnet_padding
            
            scene = (
                scene
                .cut(magnets.translate((-pip_half_height,-magnet_y, magnet_z)))
                .cut(magnets.translate((pip_half_height,-magnet_y, magnet_z)).rotate((0,0,1),(0,0,0),-self.angle))

            )
        return scene.translate((self.x_radius/2,self.y_radius/2,0))
    
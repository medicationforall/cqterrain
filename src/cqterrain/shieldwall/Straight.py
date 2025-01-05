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
from . import BaseShape, BaseMesh, BaseMagnets, BaseCut, BaseWall, ShieldShape, Mesh, Magnets

class Straight(BaseWall):
    def __init__(self):
        super().__init__()
        #properties
        self.length:float = 75
        self.width:float = 20
        self.height:float = 25

        self.base_height:float = 5.6
        
        self.render_magnets:bool = True
        self.magnet_padding:float = 1
        self.magnet_padding_x:float = 2
        
        self.cut_padding_x:float = 3
        self.cut_padding_z:float = 3
        
        self.post_length:float = 2
        self.post_padding_y:float = 1
        self.mesh_width:float = 3
        
        self.cut_width:float = .8
        self.cut_margin:float = 0.2
        self.key_margin:float = 0.5

        self.key_height:float = 2
        self.key_text:str = "Shieldwall key" 
        self.key_text_height:float = 1.5
        self.key_text_size:float = 10
        
        self.render_base_cut:bool = True
        self.base_cut_height:float|None = None
        self.base_cut_width:float|None = None
        
        #blueprints
        self.shape_bp:BaseShape = ShieldShape()
        self.mesh_bp:BaseMesh = Mesh()
        self.magnets_bp:BaseMagnets = Magnets()
        self.base_cut_bp:BaseCut = BaseCut()
        
        #shapes
        self.shape:cq.Workplane|None = None
        self.outline:cq.Workplane|None = None
        self.post:cq.Workplane|None = None
        self.key_cut:cq.Workplane|None = None
        self.key_template:cq.Workplane|None = None
        
    def __make_shape(self):
        self.shape_bp.length = self.height
        self.shape_bp.width = self.width
        self.shape_bp.base_height = self.base_height
        self.shape_bp.make()
        self.shape = self.shape_bp.build()
        
    def __make_outline(self):
        if self.shape:
            outline = (
                self.shape.extrude(self.length)
                .translate((0,0,-1*(self.length/2)))
                .rotate((0,1,0),(0,0,0),90)
            )
            self.outline = outline
        
    def _calculate_cut_height(self) -> float:
        z_diff =  self.shape_bp.base_height+4
        cut_height= self.height - z_diff
        return cut_height
        
    def __make_cut(self):
        cut_height = self._calculate_cut_height()
        cut_length = self.length - self.cut_padding_x*2
        self.cut = (
            cq.Workplane('XY')
            .box(
                cut_length,
                self.width,
                cut_height
            )
        )
        
    def __make_post(self):
        detail_height = self._calculate_cut_height()
        post_width = self.width - self.post_padding_y*2 + self.shape_bp.middle_width_inset*2 
        post = (
            cq.Workplane("XY")
            .box(
                self.post_length,
                post_width,
                detail_height
            )
        )
        self.post = post
        
    def __make_mesh(self):
        #mesh_length = self.length - 
        mesh_height = self._calculate_cut_height()
        mesh_length = self.length - self.cut_padding_x*2 - self.post_length*2
        
        self.mesh_bp.length = mesh_length
        self.mesh_bp.width = self.mesh_width
        self.mesh_bp.height = mesh_height
        self.mesh_bp.make()
        
    def __make_key_cut(self):
        cut_length = self.length - self.cut_padding_x*2 - self.post_length*2 + (self.cut_margin*2)
        cut_height = self.height - 2  + self.cut_margin
        key_length = self.length - self.cut_padding_x*2 - self.post_length*2 - (self.key_margin*2)
        key_height = self.height - 2  - self.key_margin*2
        self.key_cut = (
            cq.Workplane('XY')
            .box(
                cut_length, 
                self.cut_width, 
                cut_height
            )
        )

        logo_text = (
            cq.Workplane("XY")
            .text(self.key_text, self.key_text_size, self.key_text_height )
            .translate((-.5,0,0))
        )

        key_shape = (
            cq.Workplane('XY')
            .box(
                key_length, 
                key_height,
                self.key_height
            )
        )

        self.key_template = (
            cq.Workplane("XY")
            .union(key_shape)
            .union(logo_text.translate((0,0,self.key_height/2)))
        )
        
    def __make_magnets(self):
        self.magnets_bp.distance = self.width - self.magnets_bp.pip_radius*2 - self.magnet_padding*2 - self.magnet_padding_x
        self.magnets_bp.make()
        
    def __make_base_cut(self):
        self.base_cut_bp.length = self.length - self.cut_padding_x*2
        self.base_cut_bp.width = self.base_cut_width if self.base_cut_width else self.width - self.cut_padding_x*2
        self.base_cut_bp.height = self.base_cut_height if self.base_cut_height else self.base_height
        self.base_cut_bp.make()
        
    def make(self, parent = None):
        super().make(parent)
        self.__make_shape()
        self.__make_outline()
        self.__make_cut()
        self.__make_post()
        self.__make_mesh()
        self.__make_key_cut()
        self.__make_magnets()
        self.__make_base_cut()
        
    def build_magnets(self) -> cq.Workplane:
           magnets = self.magnets_bp.build()
           magnet_x = self.length/2 - self.magnets_bp.pip_height/2
           magnet_z = -(self.height/2) + self.base_height - self.magnets_bp.pip_radius - self.magnet_padding
           scene = (
               cq.Workplane("XY")
               .union(magnets.translate((magnet_x,0,magnet_z)))
               .union(magnets.translate((-magnet_x,0,magnet_z)))
           )
           return scene
        
    def build(self) -> cq.Workplane:
        super().build()

        interior_z_translate = 2
        post_x_translate = self.length/2-self.post_length/2 - self.cut_padding_x 
        mesh = self.mesh_bp.build()

        if self.outline and self.post and self.key_cut:
            pass
        else:
            raise Exception('Unable to resolve Straight build components')

        scene = (
            cq.Workplane('XY')
            .add(self.outline)
            .cut(self.cut.translate((
                0,
                0,
                interior_z_translate
            )))
            .add(self.post.translate((
                post_x_translate,
                0,
                interior_z_translate
            )))
            .add(self.post.translate((
                -post_x_translate,
                0,
                interior_z_translate
            )))
            .union(mesh.translate((0,0,2)))
            .cut(self.key_cut.translate((0,0,-1+self.key_margin/2)))
        )
        
        if self.render_magnets:
            magnets = self.build_magnets()
            scene = scene.cut(magnets)
            
        if self.render_base_cut:
            base_cut = self.base_cut_bp.build()
            base_cut_z = self.height/2 - self.base_cut_bp.height/2
            scene = scene.cut(base_cut.translate((0,0,-base_cut_z)))
 
        #return self.post
        return scene
        
    
    def build_assembly(self) -> cq.Assembly:
        super().build()
        interior_z_translate = 2
        post_x_translate = self.length/2-self.post_length/2 - self.cut_padding_x 
        mesh = self.mesh_bp.build()

        if self.outline and self.post and self.key_cut:
            pass
        else:
            raise Exception('Unable to resolve Straight build_assembly components')
        
        frame = (
            cq.Workplane('XY')
            .add(self.outline)
            .cut(self.cut.translate((
                0,
                0,
                interior_z_translate
            )))
            .add(self.post.translate((
                post_x_translate,
                0,
                interior_z_translate
            )))
            .add(self.post.translate((
                -post_x_translate,
                0,
                interior_z_translate
            )))
            .cut(self.key_cut.translate((0,0,-1+self.key_margin/2)))
        )
        
        if self.render_magnets:
            magnets = self.build_magnets()
            frame = frame.cut(magnets)
            
        if self.render_base_cut:
            base_cut = self.base_cut_bp.build()
            base_cut_z = self.height/2 - self.base_cut_bp.height/2
            frame = frame.cut(base_cut.translate((0,0,-base_cut_z)))

        mesh = (
            cq.Workplane('XY')
            .union(mesh.translate((0,0,2)))
            .cut(self.key_cut.translate((0,0,-1+self.key_margin/2)))
        )
        
        window = (
            cq.Workplane('XY')
            .union(self.key_cut.translate((0,0,-1+self.key_margin/2)))
        )
        
        assembly = cq.Assembly()
        assembly.add(frame, color=cq.Color(1, 0, 0), name="frame")
        assembly.add(mesh, color=cq.Color(0, 0, 1), name="mesh")
        assembly.add(window, color=cq.Color(0, 1, 0), name="window")
        
        #return self.post
        return assembly
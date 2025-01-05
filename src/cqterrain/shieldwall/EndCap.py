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
from . import ShieldShape, CapGreeble, Magnets, BaseMagnets, BaseGreeble, BaseShape, BaseWall

class EndCap(BaseWall):
    def __init__(self):
        super().__init__()
        #properties
        self.length:float = 25
        self.width:float = 20
        self.height:float = 25
        self.base_height:float = 5.6
        self.side_margin:float = -2
        self.side_height:float = 1
        self.top_height:float = 2
        
        self.cut_width:float = 3
        self.middle_width_inset:float = -6
        
        self.render_greeble:bool = True
        self.greeble_padding_y:float = 1
        
        self.render_magnets:bool = True
        self.magnet_padding:float = 1
        self.magnet_padding_x:float = 2
        
        #blueprints
        self.shape_bp:BaseShape = ShieldShape()
        self.greeble_bp:BaseGreeble = CapGreeble()
        self.magnets_bp:BaseMagnets = Magnets()
        
        #shapes
        self.end_cap:cq.Workplane|None = None
        self.greeble:cq.Workplane|None = None
        
    def __make_end_cap(self):
        self.shape_bp.length = self.height
        self.shape_bp.width = self.width
        self.shape_bp.base_height = self.base_height
        self.shape_bp.middle_width_inset = self.middle_width_inset
        
        self.shape_bp.make()
        
        self.shape_bp.width = self.height
        
        shape = (
            self.shape_bp
            .build()
            .extrude(self.length)
            .translate((0,0,-1*self.length/2))
            #.rotate((0,1,0),(0,0,0),90)
        )
        
        self.shape_bp.width = self.length*2
        self.shape_bp.base_height += self.base_height + self.side_height
        self.shape_bp.middle_width_inset = -self.length+self.cut_width
        self.shape_bp.length += 4
        self.shape_bp.make()
        cut_shape = (
            self.shape_bp
            .build()
            .extrude(self.width)
            .translate((0,0,-1*self.width/2))
            .rotate((0,1,0),(0,0,0),90)
            .rotate((0,0,1),(0,0,0),90)
            .translate((-1*(self.length/2),0,self.side_margin))
        )
        
        silhouette = (
            cq.Workplane("XY").box(
                self.length,
                self.width,
                self.height
            )
        )
        
        self.end_cap = (
            cq.Workplane('XY')
            .union(shape.rotate((0,1,0),(0,0,0),90))
            #.add(cut_shape)
            .cut(silhouette.cut(cut_shape))#)
        )
        
    def __make_greeble(self):
        self.greeble_bp.length = self.length - self.cut_width*2 +-1.5
        self.greeble_bp.width = self.width + self.middle_width_inset*2 - self.greeble_padding_y*2
        self.greeble_bp.height = self.height - self.base_height - self.side_height - self.top_height
        self.greeble_bp.make()
        
    def __make_magnets(self):
        self.magnets_bp.distance = self.width - self.magnets_bp.pip_radius*2 - self.magnet_padding*2 - self.magnet_padding_x
        self.magnets_bp.make()
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_end_cap()
        
        if self.render_greeble:
            self.__make_greeble()
            
        self.__make_magnets()
        
    def build_magnets(self) -> cq.Workplane:
           magnets = self.magnets_bp.build()
           magnet_x = self.length/2 - self.magnets_bp.pip_height/2
           magnet_z = -(self.height/2) + self.base_height - self.magnets_bp.pip_radius - self.magnet_padding
           scene = (
               cq.Workplane("XY")
               #.union(magnets.translate((magnet_x,0,magnet_z)))
               .union(magnets.translate((-magnet_x,0,magnet_z)))
           )
           return scene
        
    def build(self) -> cq.Workplane:
        super().build()
        scene = (
            cq.Workplane("XY")
            .union(self.end_cap)
        )
        
        if self.render_greeble:
            greeble = self.greeble_bp.build()
            translate_x = self.length/2 - self.greeble_bp.length/2 - self.cut_width
            translate_z = self.base_height/2+ self.side_height/2 - self.top_height/2
            scene = scene.add(greeble.translate((-translate_x,0,translate_z)))
            
        if self.render_magnets:
            magnets = self.build_magnets()
            scene = scene.cut(magnets)
        return scene
    
    def build_assembly(self) -> cq.Assembly:
        super().build()
        assembly = cq.Assembly()
        
        frame = (
            cq.Workplane("XY")
            .union(self.end_cap)
        )
        
        if self.render_magnets:
            magnets = self.build_magnets()
            frame = frame.cut(magnets)
            
        assembly.add(frame, color=cq.Color(1, 0, 0), name="frame")
        
        if self.render_greeble:
            translate_x = self.length/2 - self.greeble_bp.length/2 - self.cut_width
            translate_z = self.base_height/2+ self.side_height/2 - self.top_height/2
            greeble = (
                self.greeble_bp.build()
                .translate((-translate_x,0,translate_z))
                .cut(frame)
            )
            
            if self.greeble_bp.grill_set:
                grill_set = self.greeble_bp.grill_set.translate((-translate_x+self.greeble_bp.grill_padding_left/2,0,translate_z))
                greeble = greeble.cut(grill_set)
            assembly.add(greeble, color=cq.Color(0, 0, 1), name="mesh")
            
            if self.greeble_bp.grill_set_internal:
                grill_set_internal = self.greeble_bp.grill_set_internal.translate((-translate_x,0,translate_z))
                assembly.add(grill_set_internal, color=cq.Color(0, 1, 0), name="window")
    
        return assembly
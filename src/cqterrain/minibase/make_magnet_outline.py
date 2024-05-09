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

def make_magnet_outline(shape_height, magnet_diameter=3, magnet_height=2):
    h_radius = magnet_diameter/2
    h_solid = cq.Workplane("XY").cylinder(magnet_height, h_radius).translate((0,0,(magnet_height/2)-(shape_height/2)))
    return h_solid

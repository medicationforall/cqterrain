# Copyright 2026 James Adams
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


from . import ruin_rectangle
import random
from numpy import arange

def ruin_rectangle_random(
    length:float = 125, 
    width:float = 10, 
    height:float|None = None,
    points:int = 12,
    debug:bool = False,
    shift:tuple[float, float, float] = (-1,2,1),
    seed:str = "test"
):
    if seed:
        random.seed(seed)
    
    modifiers = arange(shift[0],shift[1]+shift[2], shift[2])
    
    adjustments = []
    for i in range(points):
        x_mod = random.choice(modifiers)
        y_mod = random.choice(modifiers)
        adjustments.append((x_mod,y_mod))
        
    return ruin_rectangle(
        length = length, 
        width = width, 
        height=height,
        points = points,
        debug=debug,
        adjustments = adjustments
    )

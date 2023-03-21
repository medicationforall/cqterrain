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

def octagon_with_dots(tile_size=5, chamfer_size = 1.2, mid_tile_size =1.6, spacing = .5 , tile_height = 1):
    tile = (cq.Workplane("XY")
            .rect(tile_size,tile_size)
            .extrude(tile_height)
            .edges("|Z")
            .chamfer(chamfer_size) # SET PERCENTAGE
            )


    mid_tile = (cq.Workplane("XY")
            .rect(mid_tile_size, mid_tile_size)
            .extrude(tile_height)
            .rotate((0,0,1),(0,0,0), 45)
            )

    tiles = (
        cq.Workplane("XY")
        .union(tile.translate((-1*((tile_size/2) + spacing/2),((tile_size/2) + spacing/2),0)))
        .union(tile.translate((((tile_size/2) + spacing/2),((tile_size/2) + spacing/2),0)))
        .union(tile.translate((((tile_size/2) + spacing/2),-1*((tile_size/2) + spacing/2),0)))
        .union(tile.translate((-1*((tile_size/2) + spacing/2),-1*((tile_size/2) + spacing/2),0)))
        .union(mid_tile)
        .union(mid_tile.translate((-1*((tile_size) + spacing),0,0)))
        .union(mid_tile.translate((((tile_size) + spacing),0,0)))
        .union(mid_tile.translate((0,-1*((tile_size) + spacing),0)))
        .union(mid_tile.translate((0,((tile_size) + spacing),0)))
        .union(mid_tile.translate((-1*((tile_size) + spacing),((tile_size) + spacing),0)))
        .union(mid_tile.translate((-1*((tile_size) + spacing),-1*((tile_size) + spacing),0)))
        .union(mid_tile.translate((((tile_size) + spacing),-1*((tile_size) + spacing),0)))
        .union(mid_tile.translate((((tile_size) + spacing),((tile_size) + spacing),0)))
    )
    return tiles.translate((0,0,-1*(tile_height/2)))


def octagon_with_dots_2(tile_size=5, chamfer_size = 1.2, mid_tile_size =1.6, spacing = .5 , tile_height = 1):
    tile = (cq.Workplane("XY")
            .box(tile_size,tile_size, tile_height)
            .edges("|Z")
            .chamfer(chamfer_size) # SET PERCENTAGE
            )


    mid_tile = (cq.Workplane("XY")
            .box(mid_tile_size, mid_tile_size, tile_height)
            .rotate((0,0,1),(0,0,0), 45)
            )

    tiles = (
        cq.Workplane("XY")
        .union(tile)
        .union(mid_tile.translate((-1*((tile_size/2) + spacing/2),((tile_size/2) + spacing/2),0)))
        .union(mid_tile.translate((((tile_size/2) + spacing/2),((tile_size/2) + spacing/2),0)))
        .union(mid_tile.translate((((tile_size/2) + spacing/2),-1*((tile_size/2) + spacing/2),0)))
        .union(mid_tile.translate((-1*((tile_size/2) + spacing/2),-1*((tile_size/2) + spacing/2),0)))
    )

    cut_tile = cq.Workplane("XY").box(tile_size+spacing, tile_size+spacing, tile_height)
    return cut_tile.intersect(tiles)

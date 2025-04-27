import cadquery as cq
from cqterrain.tile import TilesPlate

tiles_bp = TilesPlate()
tiles_bp.make()
#tiles_ex = tiles_bp.build()
tiles_ex = tiles_bp.build_assembly()

#show_object(tiles_ex)
tiles_ex.export("gltf/tiles_plate.gltf")
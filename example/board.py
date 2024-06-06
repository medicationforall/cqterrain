import cadquery as cq
from cqterrain import Board

board_bp = Board()
board_bp.length = 260
board_bp.width = 260
board_bp.height = 8
board_bp.x_count = 8
board_bp.y_count = 8
board_bp.shell = 1.5
board_bp.height_offset = 2.5

board_bp.make()
board_ex = board_bp.build()

#show_object(board_ex)
cq.exporters.export(board_ex,'stl/board_ex_full.stl')
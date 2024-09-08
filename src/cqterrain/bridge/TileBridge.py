from . import Bridge, TileStraight

class TileBridge(Bridge):
    def __init__(self):
        super().__init__()
        self.bp_straight = TileStraight()
        
    def make(self, parent=None):
        super().make(parent)
        
    def build(self):
        return super().build()
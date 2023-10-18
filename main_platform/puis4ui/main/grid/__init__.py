from res import *

class Puis4GridLayout(Layout):
    def __init__(self, model):
        super().__init__()
        self.initUI(model)
    
    def initUI(self, model):
        view = R.layout.menu
        
        self.setView(view)

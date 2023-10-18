from res import *

class Puis4MenuLayout(Layout):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        view = R.layout.menu
        
        self.setView(view)

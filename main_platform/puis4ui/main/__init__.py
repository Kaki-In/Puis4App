import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from .res import *
from .grid import *
from .menu import *

class Puis4MainLayout(Layout):
    def __init__(self, client):
        super().__init__()
        self.initUI(client)
    
    def initUI(self, client):
        view = R.layout.main_layout
        
        menu = Puis4MenuLayout()
#        grid = Puis4Gridlayout(model.grid())
        
        view.findViewById("appMainLayout").addView(menu.getView())
#        view.findViewById("appmainlayout").addView(grid)
        
        self.setView(view)
        print(view.displayString())

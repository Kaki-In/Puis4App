from .puis4ui import *
from .Puis4Client import *

class Puis4App():
    def __init__(self):
        self._ui = Puis4UI(None)
        ...
    
    def main(self):
        self._ui.main()


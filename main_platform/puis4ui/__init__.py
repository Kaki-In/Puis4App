import sys, os
from .main import *

class Puis4UI( ):
    def __init__(self, client):
        self._layout = Puis4MainLayout(client)
    
    def main(self):
        self._layout.show()
        self._layout.main()


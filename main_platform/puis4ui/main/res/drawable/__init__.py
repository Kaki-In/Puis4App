from Qinter import R, Path
import os

__DIRNAME__ = os.path.abspath(os.path.dirname(__file__))

def __init__(dirname):
    for file in os.listdir(__DIRNAME__ + os.path.sep + dirname):
        a = file.split(".")
        if len(a) != 2:
            continue
        filename, extension = a
        if extension == "png":
            setattr(R.src, dirname + "_" + filename, Path(__DIRNAME__ + os.path.sep + dirname + os.path.sep + file))

__init__("icons")
__init__("images")

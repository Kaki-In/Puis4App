from Qinter import R, parser
import os

__DIRNAME__ = os.path.abspath(os.path.dirname(__file__))

def __init__(dirpath):
    dirpath_string = __DIRNAME__
    for i in dirpath:
        dirpath_string += os.path.sep + i
    if dirpath:
        dirname = dirpath[ -1 ]
    else:
        dirname = ""
    for file in os.listdir(dirpath_string):
        a = file.split(".")
        if len(a) == 1:
            __init__(dirpath + [file])
        if len(a) != 2:
            continue
        filename, extension = a
        if extension == "xml":
            readingFile = open(dirpath_string + os.path.sep + file, "r")
            data = readingFile.read()
            readingFile.close()
            try:
                setattr(R.layout, dirname + ("_" if dirname else "") + filename, parser.parse(data).getViews() [0])
            except Exception as exc:
                raise SyntaxError(dirpath_string + os.path.sep + file)

__init__([])

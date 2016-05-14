import sys
from JuggleHelpers import *
#from JuggleSettings import *

def juggleParseLine(line):
    global inJuggleMode
    global currentLanguage
    if inJuggleMode:
        if closeTag in line:
            end = line.find(closeTag)
            juggleInterpret(line[:end])
            inJuggleMode = False
            juggleParseLine(line[end+len(closeTag):])
        else:
            juggleInterpret(line,currentLanguage)
    else:
        if openTag in line:
            end = line.find(openTag)
            saveUserCode(line[:end])
            inJuggleMode = True
            juggleParseLine(line[end+len(openTag):])
        else:
            saveUserCode(line,currentLanguage)

try:
    codeFile = open(sys.argv[0])
except IOerror:
    print("Could not Open: "+sys.argv[0])
    sys.exit()

for line in codeFile:
    juggleParseLine(line)

for language in languages:
    name = language["name"]
    ext = language["extension"]
    #TODO: compile and run code that has been written.



codeFile.close()

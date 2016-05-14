import JuggleLanguages.*
from JuggleSettings import *

inJuggleMode = False
currentLanguage = None

def getLang():


def juggleInterpret(str,lang):


def saveUserCode(str,lang):



def saveVariable(varName,fromLang,toLang):
    if toLang == None:
        for language in languages:
            saveVariable(varName,fromLang,language)
    else


def saveFunction(funcName,fromLang,toLang):
    if toLang == None:
        for language in languages:
            saveFunction(funcName,fromLang,language)
    else:

from lib.file_manager import *
from lib.place_holder import *
import pyautogui as pya
import time


isloop = True
desiredPath = "gittemp"

def logMenu():
    clear()
    
    logFile(desiredPath,input('give me reason to:'))
    print('writen file done')
    time.sleep(2.3)



def readMenu():
    clear()

    readFile(desiredPath)
    input('press enter to go back  ')



def gitHelper():
    pass
    print('1) set up git',end="")
    print('       2) add && commit',"\n")


    input('enter to close')
    







while isloop:
    clear()
    print('MENU 1. for xxx || 2. for yyy :  ',end="")
    inp = int(input())

    match(inp):
        case 1:
            logMenu()

            
        case 2:
            readMenu()

        case 3:
            gitHelper()


        case _:
            isloop = False
            

            




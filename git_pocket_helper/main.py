from lib.file_manager import *
from lib.place_holder import *
import pyautogui as pya
import time
isloop = True
desiredPath = "gittemp"
while isloop:
    clear()
    print('MENU 1. for xxx || 2. for yyy :  ',end="")
    inp = int(input())

    match(inp):
        case 1:
            clear()
            
            logFile(desiredPath,input('give me reason to:'))
            print('writen file done')
            time.sleep(2.3)
            
        case 2:
            clear()

            readFile(desiredPath)
            input('press enter to go back  ')
            
        case 3:
            isloop = False
            

            




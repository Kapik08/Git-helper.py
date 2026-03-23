from lib.file_manager import *
from lib.place_holder import *
import pyautogui as pya
import time


cc_GIT_PATH = acces_file("config/customPath.txt")

isloop = True
GIT_Path = "" 
configPath = "configPath"


if cc_GIT_PATH == "":
    GIT_Path = 'gittemp'
else:
    GIT_Path = cc_GIT_PATH



def basePanel():
    clear()

    print("||enter 1 for File write || 2 for File read ||")
    print("||enter 3 for GIT Helper || 4 for Settings  ||")



def logMenu():
    clear()
    
    logFilea(GIT_Path,input('give me reason to:'))
    print('writen file done')
    time.sleep(2.3)



def readMenu():
    clear()

    readFile(GIT_Path)
    input('press enter to go back  ')



def gitHelper():
    clear()


    print('1) set up git',end="")
    print('       2) add && commit',"\n")
    print('3. Place Holder',end="")
    print('       4. Lorem ','\n')


    input('enter to close')
    
def settings():
    
    customPath = input('nazwij file path/name : ')
    logFilew("config/customPath.txt",customPath)
    input("it is adwised to restart the program to make sure it works properly")

def test():
    
    x = acces_file("config/customPath.txt")
    print(x)
    input()




while isloop:
    
    basePanel()
    inp = int(input())

    match(inp):
        case 1:
            logMenu()

        case 2:
            readMenu()

        case 3:
            gitHelper()


        case 4:
            settings()
        
        case 5:
            test()

        case _:
            isloop = False
            
print('koniec programu')
            




from lib.file_manager import *
from lib.place_holder import *
import pyautogui as pya
import time


cc_GIT_PATH = acces_file("config/customPath.txt")

isloop = True
GIT_Path = "" 
configPath = "configPath"

# if custom path exists set GIT path to custom one 
# else set it do default
if cc_GIT_PATH == "":
    GIT_Path = 'gittemp.txt'
else:
    GIT_Path = cc_GIT_PATH + ".txt"
    GIT_Path.replace(" ","_")



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
    clear()

    print("1) for custom git path || press 0 to go back","\n",)
    match(int(input("enter num for what you wanna change "))):

        case 1:
            settingsCC_path()

        case 2:
            pass
        case 0:
            pass

def settingsCC_path():
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
            




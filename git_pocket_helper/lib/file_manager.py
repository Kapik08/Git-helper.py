def logFilea(fileName:str,content:str):

    with open(fileName,"a") as f:    
        f.write(content + "\n")

def logFilew(fileName:str,content:str):

    with open(fileName,"w") as f:    
        f.write(content)

#returns first line of file
def acces_file(fileName: str):

    with open(fileName) as f:
        return f.readline()

def readFile(fileName: str):
    i = 0
    with open(fileName) as f:
        for line in f:
            i+=1
            print(i,". ",line)    
        
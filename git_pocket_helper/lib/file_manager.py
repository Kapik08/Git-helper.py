def logFile(fileName,content):

    with open(fileName,"a") as f:    
        f.write(content + "\n")
                
def readFile(fileName):
    i = 0
    with open(fileName) as f:
        for line in f:
            i+=1
            print(i,". ",line)    
        
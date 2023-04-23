from random import randint as rand

def Log(path, ToLog):
    logpath = open(path, "a")
    logpath.truncate(0)
    for i in range(len(ToLog)):
        logpath.write(ToLog[i] + "\n")     
    logpath.flush()
    logpath.close()
    
def Determine(digits: int) -> int:
    return pow(10, digits)

def GetAll(digits: int) -> tuple:
    possibilites = []
    amount = Determine(digits)   
     
    n=""
    
    while(len(possibilites) < amount):
        for i in range(digits):
            n += str(rand(0, 9))
        possibilites.append(n)
        n = ""
    
    Log("_logs.txt", possibilites)
    return possibilites
        
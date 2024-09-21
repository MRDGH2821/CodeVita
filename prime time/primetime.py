line = input().split()
totalHours = int(line[0])
parts = int(line[1])

def isPrime(number: int):
    primeFlag = False
    if number == 1: 
        primeFlag = False
    elif number == 2:
        primeFlag = True
    else:
        for i in range(2, number):
            if number%i == 0:
                primeFlag = False
                break
            else: 
                primeFlag = True

    return primeFlag

primeHours = [x for x in range(0, totalHours+1) if isPrime(x)]

def isStagePass(num):
    if num>totalHours:
        return False
    else: 
        return isPrime(num)

def isAllStagePass(num):
    flag = False   
    for _ in range(parts):
        if isStagePass(num):
            flag = True
            num = num + 12
        else:
            flag = False
    return flag

equivalentPrimeHours = [x for x in primeHours if isAllStagePass(x)]

print(len(equivalentPrimeHours))
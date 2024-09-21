line1 = input().split()
line2 = input().split()

numberQty = int(line1[0])
rangeStep = int(line1[1])
numbers = [int(x) for x in line2]


def isHappy(num):
    boundary = [x for x in range(num-rangeStep, num+rangeStep+1) if x != num]

    flag = False

    for i in numbers:
        if i in boundary:
            flag = True
            break
        else:
            flag = False

    return flag


def main():
    happinessQty = 0
    for i in numbers:
        if isHappy(i):
            happinessQty = happinessQty + 1

    return happinessQty


print(main())

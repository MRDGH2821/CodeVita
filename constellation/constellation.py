"""
columns = int(input())
line1 = input()
line2 = input()
line3 = input()
"""

columns = 18
line1 = '*.*#***#***#***.*.'
line2 = '*.*#*.*#.*.#******'
line3 = '***#***#***#****.*'



def extractColumn(columnNum):
    num = columnNum
    return [line1[num], line2[num], line3[num]]


def isDotColumn(columnNum):
    column = extractColumn(columnNum)
    return column[0] == '.' and column[1] == '.' and column[2] == '.'


def isPoundColumn(columnNum):
    column = extractColumn(columnNum)
    return column[0] == '#' and column[1] == '#' and column[2] == '#'


def isColumnMatch(column1, column2):
    return column1[0] == column2[0] and column1[1] == column2[1] and column1[2] == column2[2]


def isLetterU(columnNum):
    flag = False
    for i in range(columnNum, columnNum+3):
        if isDotColumn(i):
            flag = False
        elif isPoundColumn(i):
            flag = False
        else:
            flag = True

    if flag == False:
        return False

    column1 = extractColumn(columnNum)
    column2 = extractColumn(columnNum+1)
    column3 = extractColumn(columnNum+2)

    data1 = ['*', '*', '*']
    data2 = ['.', '.', '*']
    data3 = ['*', '*', '*']

    return isColumnMatch(column1, data1) and isColumnMatch(column2, data2) and isColumnMatch(column3, data3)


def isLetterO(columnNum):
    flag = False
    for i in range(columnNum, columnNum+3):
        if isDotColumn(i):
            flag = False
        elif isPoundColumn(i):
            flag = False
        else:
            flag = True

    if flag == False:
        return False

    column1 = extractColumn(columnNum)
    column2 = extractColumn(columnNum+1)
    column3 = extractColumn(columnNum+2)

    data1 = ['*', '*', '*']
    data2 = ['*', '.', '*']
    data3 = ['*', '*', '*']

    return isColumnMatch(column1, data1) and isColumnMatch(column2, data2) and isColumnMatch(column3, data3)


def isLetterI(columnNum):
    flag = False
    for i in range(columnNum, columnNum+3):
        if isDotColumn(i):
            flag = False
        elif isPoundColumn(i):
            flag = False
        else:
            flag = True

    if flag == False:
        return False

    column1 = extractColumn(columnNum)
    column2 = extractColumn(columnNum+1)
    column3 = extractColumn(columnNum+2)

    data1 = ['*', '.', '*']
    data2 = ['*', '*', '*']
    data3 = ['*', '.', '*']

    return isColumnMatch(column1, data1) and isColumnMatch(column2, data2) and isColumnMatch(column3, data3)


def isLetterE(columnNum):
    flag = False
    for i in range(columnNum, columnNum+3):
        if isDotColumn(i):
            flag = False
        elif isPoundColumn(i):
            flag = False
        else:
            flag = True

    if flag == False:
        return False

    column1 = extractColumn(columnNum)
    column2 = extractColumn(columnNum+1)
    column3 = extractColumn(columnNum+2)

    data1 = ['*', '*', '*']
    data2 = ['*', '*', '*']
    data3 = ['*', '*', '*']

    return isColumnMatch(column1, data1) and isColumnMatch(column2, data2) and isColumnMatch(column3, data3)


def isLetterA(columnNum):
    flag = False
    for i in range(columnNum, columnNum+3):
        if isDotColumn(i):
            flag = False
        elif isPoundColumn(i):
            flag = False
        else:
            flag = True

    if flag == False:
        return False

    column1 = extractColumn(columnNum)
    column2 = extractColumn(columnNum+1)
    column3 = extractColumn(columnNum+2)

    data1 = ['.', '*', '*']
    data2 = ['*', '*', '.']
    data3 = ['.', '*', '*']

    return isColumnMatch(column1, data1) and isColumnMatch(column2, data2) and isColumnMatch(column3, data3)


def main():
    letters = []
    for i in range(columns-2):
        if isDotColumn(i):
            letters.append('')
        if isPoundColumn(i):
            letters.append('#')
        if isLetterA(i):
            letters.append('A')
        if isLetterE(i):
            letters.append('E')
        if isLetterI(i):
            letters.append('I')
        if isLetterO(i):
            letters.append('O')
        if isLetterU(i):
            letters.append('U')

    return "".join(letters)


print(main())

def matrixPart(partStr, length):
    # matrix1
    keyMatrix = []
    for i in range(0, length):
        keyMatrix.append(range(0, length))

    for i in range(0, length):
        for j in range(0, length):
            keyMatrix[i][j] = partStr[i*length+j]

    # matrix2
    Tpart = []
    for i in range(0, length):
        Tpart.append(range(0, length))

    for i in range(0, length):
        for j in range(0, length):
            Tpart[i][j] = keyMatrix[j][i]

    reStr = ''
    for i in range(0, length):
        for j in range(0, length):
            reStr += Tpart[i][j]

    return reStr

def matrixDecode(sourceStr, key):
    matrixLen = int(key[0])
    while len(sourceStr) < matrixLen * matrixLen:
        matrixLen -= 1

    matrixSquare = matrixLen * matrixLen

    if (len(sourceStr) % matrixSquare) != 0:
        numA = matrixSquare
        latterStr = sourceStr[:numA]
        realLatter = matrixPart(latterStr, matrixLen)
        firstStr = sourceStr[numA:]
        tmpStr = realLatter + firstStr
        sourceStr = tmpStr[::-1]

    matrixNum = len(sourceStr) / matrixSquare
    numA = 0
    numB = 0
    numB += matrixSquare
    reStr = ''
    for i in range(0, matrixNum):
        sToT = sourceStr[numA:numB]
        reStr += matrixPart(sToT, matrixLen)
        numA += matrixSquare
        numB += matrixSquare

    reStr += sourceStr[numA:]
    return reStr

s = raw_input("input: ")
key = raw_input("key: ")
endS = matrixDecode(s, key)
print endS

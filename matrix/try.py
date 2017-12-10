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

def matrixEncode(sourceStr, key):
    matrixLen = int(key[0])
    while len(sourceStr) < matrixLen * matrixLen:
        matrixLen -= 1

    matrixSquare = matrixLen * matrixLen

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

    if (len(sourceStr) % matrixSquare) != 0:
        latterStr = sourceStr[numA:]
        secondStr = reStr + latterStr
        secondStr = secondStr[::-1]

        numA = matrixSquare
        sToT = secondStr[0:numA]
        reStr = matrixPart(sToT, matrixLen)
        reStr += secondStr[numA:]

    return reStr

s = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=+'
endS = matrixEncode(s, '12')
print endS

#-*- coding:utf-8 -*-
#! myEncode python script

import base64

def xorEncode(sourceStr, key):
    keyList = []
    for i in range(0, len(key)):
        keyList.append(int(key[i]))

    strList = []
    for i in range(0, len(sourceStr)):
        strList.append(ord(sourceStr[i]))

    endCode = []
    j = 0
    keyLen = len(keyList)
    for i in range(0, len(strList)):
        endCode.append(keyList[j] ^ strList[i])
        j += 1
        if j== keyLen:
            j = 0

    endStr = ''
    for i in range(0, len(endCode)):
        endStr += chr(endCode[i])

    return endStr

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

# main
sourceName = raw_input('请输入要加密的文件路径: ')
try:
    sourceFile = file(sourceName, 'r')
except:
    print("错误：源文件不存在")
    exit()

targetName = raw_input('请输入要保存文件路径: ')
try:
    targetFile = file(targetName, 'w+')
except:
    print("错误：创建文件失败")
    exit()

keyLen = 0
while keyLen<2:
    keyStr = raw_input('请输入整数密码(至少2位): ')
    keyLen = len(keyStr)
    if keyLen<2:
        print("错误: 请输入至少2位的整数密码")

text = sourceFile.read()
code1 = xorEncode(text, keyStr)
del text

code2 = matrixEncode(code1, keyStr)
del code1

code = base64.b64encode(code2)
del code2

targetFile.write(code)
sourceFile.close()
targetFile.close()

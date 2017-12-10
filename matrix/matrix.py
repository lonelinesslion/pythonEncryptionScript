# -*- coding:utf-8 -*-

s = raw_input("input: ")
print len(s)

a = [range(0, 3)]
for i in range(1, 3):
    a.append(range(0, 3))

for i in range(0, 3):
    for j in range(0, 3):
        a[i][j] = s[i*3+j]

b = a
for i in range(0, 3):
    for j in range(0, 3):
        b[i][j] = a[j][i]

tmpS = ''
for i in range(0, 3):
    for j in range(0, 3):
        tmpS += b[i][j]

for i in range(9, len(s)):
    tmpS += s[i]

a = []
for i in range(0, len(tmpS)):
    a.append(tmpS[i])

c = a[::-1]
b = [range(0, 3)]
for i in range(1, 3):
    b.append(range(0, 3))

for i in range(0, 3):
    for j in range(0, 3):
        b[i][j] = c[i*3+j]

c = b
for i in range(0, 3):
    for j in range(0, 3):
        b[i][j] = c[j][i]

tmpS = ''
for i in range(0, 3):
    for j in range(0, 3):
        tmpS += b[i][j]

print tmpS

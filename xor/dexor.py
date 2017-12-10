# -*- coding:utf-8 -*-
# xor decode algorithm

filename = raw_input("file: ")
key = raw_input("key: ")

f = file(filename, 'r')
s = f.read()

keylist = []
for i in range(0, len(key)):
    keylist.append(int(key[i]))

slist = []
for i in range(0, len(s)):
    slist.append(ord(s[i]))

endlist = []
j = 0
keyLen = len(keylist)
for i in range(0, len(slist)):
    endlist.append(keylist[j] ^ slist[i])
    j += 1
    if j== keyLen:
        j = 0

endString = ''
for i in range(0, len(endlist)):
    endString += chr(endlist[i])

print endlist
print endString

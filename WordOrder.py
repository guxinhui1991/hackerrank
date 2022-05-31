# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

N = int(input())
inStr = []

for i in range(N):
    word = input()
    inStr.append(word)

wordDic = {}
for i in inStr:
    if i in wordDic.keys():
        wordDic[i] = wordDic[i] + 1
    else:
        wordDic[i] = 1

print(str(len(wordDic.keys())))
for i in wordDic.keys():
    sys.stdout.write(str(wordDic[i]) + ' ')
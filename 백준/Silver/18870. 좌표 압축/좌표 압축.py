import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

numset = sorted(set(num))
dic = {numset[i] : i for i in range(len(numset))}

for i in num:
    print(dic[i], end=" ")

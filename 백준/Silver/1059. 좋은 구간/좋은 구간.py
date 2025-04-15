import sys
input = sys.stdin.readline
L = int(input())
num = list(map(int, input().split()))
n = int(input())
num.sort()

if n in num:
    print(0)
else:
    min = 0
    max = 0
    for i in num:
        if i < n:
            min = i
        elif i > n and max == 0:
            max = i
    max -= 1
    min += 1
    print((n-min)*(max-n+1)+(max-n))

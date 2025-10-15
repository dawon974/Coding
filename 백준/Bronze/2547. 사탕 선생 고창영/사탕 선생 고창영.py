import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    empty = input()
    n = int(input())
    sum = 0
    for j in range(n):
        sum+=int(input())
    if sum%n == 0:
        print('YES')
    else:
        print('NO')
    
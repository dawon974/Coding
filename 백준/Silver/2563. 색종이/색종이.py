import sys
input = sys.stdin.readline

N = int(input())

arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    X, Y = map(int, input().split())
    for i in range(X, X+10):
        for j in range(Y, Y+10):
            arr[i][j] = 1
res = 0
for i in arr:
    res+=sum(i)
    
print(res)
import sys
input = sys.stdin.readline

A = []
max_value = 0
row = 0
col = 0

for _ in range(9):
    a = list(map(int,input().split()))
    A.append(a)

for i in range(9):
    for j in range(9):
        if A[i][j] >= max_value:
            max_value = A[i][j]
            row = i+1
            col = j+1
    
print(max_value)
print(row, col)
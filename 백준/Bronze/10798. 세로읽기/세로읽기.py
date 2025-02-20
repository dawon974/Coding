import sys
input = sys.stdin.readline

w = []

for i in range(5):
    a = list(input().strip())
    w.append(a)

for j in range(15):
    for i in range(5):
        if j < len(w[i]):
            print(w[i][j], end='')
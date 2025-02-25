import sys
input = sys.stdin.readline

n = int(input())
number = []

for _ in range(n):
    N = int(input())
    if N == 0 :
        number.pop()
    else:
        number.append(N)
print(sum(number))
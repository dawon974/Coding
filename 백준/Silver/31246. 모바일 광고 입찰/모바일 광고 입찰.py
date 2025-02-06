import sys
input = sys.stdin.readline

a,b = map(int, input().split())
x = []

for _ in range(a):
    A,B = map(int, input().split())
    x.append(B-A)
x.sort()

if x[b-1] < 0:
    print(0)
else :
    print(x[b-1])
    
    
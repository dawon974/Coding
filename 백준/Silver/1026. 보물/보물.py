import sys

input=sys.stdin.readline

N=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

s=0
a.sort()
for i in range(N):
    A=a[i]
    B=b.pop(b.index(max(b)))

    s+=A*B
print(s)
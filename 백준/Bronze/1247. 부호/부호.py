import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    s=0
    for i in range(N):
        s+=int(input())
    if s==0:
        print(0)
    elif s>0 :
        print("+")
    else:
        print("-")
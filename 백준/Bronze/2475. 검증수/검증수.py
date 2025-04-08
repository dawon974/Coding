import sys
input = sys.stdin.readline
K = list(map(int, input().split()))
cnt=0

for i in K:
    cnt+=i**2
print(cnt%10)
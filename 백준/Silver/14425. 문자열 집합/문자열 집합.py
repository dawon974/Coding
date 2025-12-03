import sys
input = sys.stdin.readline

cnt = 0
n,m = map(int, input().split())

li = set()
for i in range(n):
    li.add(input())

for j in range(m):
    s_ = input()
    
    if s_ in li:
        cnt+=1
print(cnt)
    
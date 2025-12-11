from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

q = deque([])
for i in range(n):
    if a[i] == 0:
        q.append(b[i])
        
for j in range(m):
    q.appendleft(c[j])
    print(q.pop(), end = ' ')
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
result = []

while q:
    #언패킹
    idx, bp = q.popleft()
    result.append(idx+1)
    
    if bp > 0 :
        q.rotate(-(bp-1))
    elif bp < 0:
        q.rotate(-bp)
print(' '.join(map(str, result)))
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    command = list(map(int, input().split()))
    
    if command[0] == 1:
        q.appendleft(command[1])
    elif command[0] == 2:
        q.append(command[1])
    elif command[0] == 3:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
            
    elif command[0] == 4:
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
            
    elif command[0] == 5:
        print(len(q))
        
    elif command[0] == 6:
        if len(q) == 0:
            print(1)
        else:
            print(0)
            
    elif command[0] == 7:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            
    elif command[0] == 8:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
def bfs(start):
    q = deque([start])
    
    while q:
        node = q.popleft()
        
        for j in graph[node]:
            if visited[j] == 0:
                visited[j] = node
                q.append(j)
bfs(1)
answer = visited[2:]
for x in answer:
    print(x)
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
#행렬
graph = [[] for _ in range(n+1)]

#최단거리
distance = [0] * (n+1)

#방문 리스트
visited = [False] * (n+1)

#단방향 도로 처리
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

#bfs 함수
def bfs(start) :
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while q :
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end = '\n')
bfs(x)

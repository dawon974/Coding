import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

#행렬 만들기
graph = [[] for _ in range(N+1)]
#양방향 간선 연결
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
count = 0
#방문 리스트 행렬
visited = [False] * (N+1)

#dfs 알고리즘
def dfs(x):
    visited[x] = True
    global count
    for i in graph[x]:
        if not visited[i]:
            count+=1
            dfs(i)
dfs(1)
print(count)
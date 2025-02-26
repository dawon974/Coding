from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, k = map(int, input().split())
#바이러스에 대한 정보를 담는 리스트
virus = []

for i in range(n):
    virus.append(list(map(int, input().split())))

#시간, 행, 열     
S, X, Y = map(int, input().split())

q = []
for i in range(n):
    for j in range(n):
        if virus[i][j] != 0:
            q.append((virus[i][j], i, j, 0))
            
#리스트로 받아 정렬 후 queue로 변경
q.sort()
q = deque(q)

#dfs
while q :
    viru, row, col, time = q.popleft()
    if time == S :
        break
    for i in range(4):
        r = row + dx[i]
        c = col + dy[i]
        if -1 < r < n and -1 < c < n and not virus[r][c]:
            virus[r][c] = viru
            q.append((viru, r, c, time + 1))
print(virus[X-1][Y-1])
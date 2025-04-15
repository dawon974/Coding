import sys
input = sys.stdin.readline

N = int(input())
Tree = list(map(int, input().split()))
D = int(input())

def dfs(del_node):
    Tree[del_node] = -10
    for i in range(N):
        if del_node == Tree[i]:
            dfs(i)
dfs(D)
cnt = 0
for i in range(N):
    if Tree[i] != -10 and i not in Tree:
        cnt+=1
print(cnt)
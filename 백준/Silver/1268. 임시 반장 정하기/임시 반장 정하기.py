N = int(input())

c=[]
same = [0] * N

for i in range(N):
    c.append(list(map(int, input().split())))
    same[i] = [0]*N

for i in range(5):
    for j in range(N):
        for k in range(j+1, N):
            if c[j][i] == c[k][i]:
                same[k][j] = 1
                same[j][k] = 1

cnt=[]
for s in same:
    cnt.append(s.count(1))
print(cnt.index(max(cnt))+1)
        
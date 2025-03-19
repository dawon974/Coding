N,M = map(int,input().split())
cnt = 0

#행렬 A,B 입력받기
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

#3x3행렬 생성
def matrix(i, j, arr):
    for x in range(i, i+3):
        for y in range(j, j+3):
            arr[x][y] ^= 1
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            matrix(i, j, A)
            cnt+=1

# 최종 비교
if A == B:
    print(cnt)
else:
    print(-1)
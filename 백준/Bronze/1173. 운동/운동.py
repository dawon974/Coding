import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())
cnt = 0 #운동 횟수
total = 0 # 총 운동시간
heart = m #초기 맥박

#만약 운동 할 수 없다면 -1을 출력
if m+T > M:
    print(-1)
else:
    while cnt < N:
        if heart+T <= M :
            heart += T
            cnt+=1
            total+=1
        else:
            heart-=R
            #맥박수는 초기 맥박 아래로 내려가지 않는다.
            if heart < m:
                heart = m
            total+=1
    print(total)
        
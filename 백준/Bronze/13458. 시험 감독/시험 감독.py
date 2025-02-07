import sys
input = sys.stdin.readline

N = int(input()) #시험장의 개수
arr = list(map(int, input().split())) #각 시험장에 있는 응시자의 수
b,c = map(int, input().split()) #총감독관이 감시할 수 있는 응시자의 수가 B, 부감독관이 감시할 수 있는 응시자의 수가 C.
cnt=0

for i in range(N) :
    arr[i]-=b
    cnt+=1
    if arr[i]>0:
        if arr[i]%c == 0:
            cnt+=(arr[i]//c)
        else:
            cnt+=(arr[i]//c+1)
print(cnt)
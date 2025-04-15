num = list(map(int, input().split()))
N = 1
while True:
    cnt=0
    for i in num:
        if N%i == 0:
            cnt+=1
    if cnt >= 3:
        print(N)
        break
    N+=1
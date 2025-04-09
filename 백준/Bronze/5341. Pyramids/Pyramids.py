while True:
    sum=0
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n,0,-1):
            sum+=i
        print(sum)
            
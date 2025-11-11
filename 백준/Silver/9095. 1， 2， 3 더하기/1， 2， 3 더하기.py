import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    dp = [0,1,2,4,7]
    for i in range(5,n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[n])
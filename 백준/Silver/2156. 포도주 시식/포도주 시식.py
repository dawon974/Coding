n = int(input())

g = [0]*10001
for i in range(n):
    g[i] = int(input())

dp = [0]*10001
dp[0] = g[0]
dp[1] = g[0]+g[1]
dp[2] = max(g[0]+g[2], g[1]+g[2], dp[1])

for i in range(3, n):
    dp[i] = max(g[i]+dp[i-2], g[i]+g[i-1]+dp[i-3], dp[i-1])
print(max(dp))
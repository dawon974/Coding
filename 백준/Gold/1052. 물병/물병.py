N, K = map(int, input().split())

answer = 0

while bin(N).count('1') > K :
    idx = bin(N)[::-1].index('1')
    answer+=2**idx
    N+=2**idx
print(answer)
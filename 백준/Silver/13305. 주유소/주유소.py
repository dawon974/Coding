import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))
price = list(map(int, input().split()))
    
price_min = price[0]
total = line[0] * price[0]

for i in range(1, N-1):
    if price_min > price[i]:
        price_min = price[i]
    total+=price_min * line[i]
print(total)
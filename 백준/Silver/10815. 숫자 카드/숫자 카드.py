import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

dict = {}

for i in range(len(card)):
    dict[card[i]] = 0
 
for j in range(m):
    if check[j] in dict:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
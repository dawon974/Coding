import sys
input = sys.stdin.readline

n = int(input())
ca = list(map(int, input().split()))

m = int(input())
ch = list(map(int, input().split()))

dic = {}
for i in range(len(ca)):
    dic[ca[i]] = 0
    
for j in range(m):
    if ch[j] in dic:
        print(1, end= ' ')
    else:
        print(0, end= ' ')
    
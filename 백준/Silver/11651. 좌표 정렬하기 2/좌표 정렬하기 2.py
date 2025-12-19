n = int(input())

li = []

for i in range(n):
    x, y = map(int, input().split())
    li.append((x,y))
    
li.sort(key = lambda x : (x[1], x[0]))

for k in li:
    print(k[0], k[1])
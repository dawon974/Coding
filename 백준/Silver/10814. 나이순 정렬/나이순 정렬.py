n = int(input())
user = []

for i in range(n):
    old, name = map(str, input().split())
    old = int(old)
    user.append((old, name))
    
user.sort(key = lambda x : (x[0]))

for i in user:
    print(i[0], i[1])
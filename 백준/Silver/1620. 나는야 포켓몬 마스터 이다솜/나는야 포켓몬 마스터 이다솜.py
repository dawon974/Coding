import sys
input = sys.stdin.readline

n, m = map(int, input().split())
    
dic = {}

for i in range(1,n+1):
    name = input().rstrip()
    dic[i] = name
    dic[name] = i
    
for i in range(m):
    pro = input().rstrip()
    if pro.isdigit():
        print(dic[int(pro)])
    else:
        print(dic[pro])
    
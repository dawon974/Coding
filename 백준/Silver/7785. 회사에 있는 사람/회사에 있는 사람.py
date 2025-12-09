import sys
input = sys.stdin.readline

n = int(input())
dic = dict()

for _ in range(n):
    name, record = map(str, input().split())
    
    if record == 'enter':
        dic[name] = record
    else:
        del dic[name]
        
dic = sorted(dic.keys(), reverse = True)

for i in dic:
    print(i)

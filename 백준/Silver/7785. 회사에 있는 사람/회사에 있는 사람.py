import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    name, record = map(str, input().split())
    
    if record == "enter":
        dic[name] = record
    else:
        del dic[name]
       
dic = sorted(dic.keys(), reverse = True)

for j in dic:
    print(j)
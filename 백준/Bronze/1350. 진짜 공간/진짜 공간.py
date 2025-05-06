n = int(input())
li = list(map(int, input().split()))
m = int(input())
    
result = 0

for i in li:
    if i % m == 0:
        result += i // m
    else:
        result += i // m+1
print(result * m)
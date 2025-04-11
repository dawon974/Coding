import math

n, k, l = map(int, input().split())
cnt = 0

while True:
    if math.ceil(k) == math.ceil(l):
        break
    else:
        k = math.ceil(k/2)
        l = math.ceil(l/2)
        cnt+=1
print(cnt)
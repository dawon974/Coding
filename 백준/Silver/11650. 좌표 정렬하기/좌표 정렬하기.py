N = int(input())
arr = []

for i in range(N):
    x,y = map(int, input().split())
    arr.append((x,y))
arr.sort()
for i in range(N):
    print(arr[i][0], arr[i][1])
    
n = int(input())

for i in range(1, n + 1):
    first = input().strip()   # 이름
    last = input().strip()    # 성
    
    print("Case " + str(i) + ": " + last + ", " + first)

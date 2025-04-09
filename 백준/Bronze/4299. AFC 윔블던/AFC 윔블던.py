a, b = map(int, input().split())

if a+b <0 or a-b <0 or (a+b) %2:
    print(-1)
else:
    S = (a+b)//2
    D = abs(S-b)
    print(max(S,D), min(S,D))
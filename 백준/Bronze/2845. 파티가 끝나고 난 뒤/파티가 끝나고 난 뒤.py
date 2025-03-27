L, P = map(int, input().split())

party = list(map(int, input().split()))
for i in party:
    print(i-L*P, end = ' ')
    
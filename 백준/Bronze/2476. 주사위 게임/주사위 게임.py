n = int(input())
dice = 0
    
for _ in range(n):
    a, b, c = map(int, input().split())
    
    if a == b == c :
        dice = max(dice, 10000+a*1000)
    elif a == b:
        dice = max(dice, 1000+a*100)
    elif b == c:
        dice = max(dice, 1000+b*100)
    elif c == a:
        dice = max(dice, 1000+c*100)
    else:
        dice = max(dice, max(a,b,c)*100)
print(dice)
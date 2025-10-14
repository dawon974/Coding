a, b, c = map(int,input().split())

if a==b==c:
    print(2)
elif a*a+b*b == c*c or b*b+c*c == a*a or c*c+a*a == b*b:
    print(1)
else:
    print(0)
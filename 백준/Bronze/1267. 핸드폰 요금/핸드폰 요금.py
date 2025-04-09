N = int(input())
T = list(map(int, input().split()))

y=m=0

for i in T:
    y += (i//30+1)*10
    m += (i//60+1)*15
if y>m :
    print("M", m)
elif y == m :
    print("Y M", m)
else:
    print("Y", y)
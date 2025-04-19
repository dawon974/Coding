people = []
total = 0

for i in range(4):
    a,b = list(map(int, input().split()))
    total-=a
    total+=b
    people.append(total)
print(max(people))
N = int(input())
player = []
result = []

for _ in range(N):
    a = input()
    player.append(a[0])
first_name = set(player)

for i in first_name:
    if player.count(i) >= 5:
        result.append(i)
if len(result) > 0:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")
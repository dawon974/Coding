N, L, D = map(int, input().split())
#앨범 총 길이
total = (N*L) + (N-1) * 5
song = [False] * total

for i in range(0, total, L+5):
    for j in range(i, i+L):
        song[j] = True
for i in range(0, total, D):
    if not song[i]:
        print(i)
        break
else:
    print(i + D)

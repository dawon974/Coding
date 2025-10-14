n = int(input())
student = [input() for _ in range(n)]
correct = [input() for _ in range(n)]
cnt = 0

for i in range(n):
    if student[i] == correct[i]:
        cnt+=1
print(cnt)
    
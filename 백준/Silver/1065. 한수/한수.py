N = int(input())
cnt = 0
for i in range(1, N+1):
    num_list = list(map(int, str(i)))
    if i <= 99:
        cnt+=1
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        cnt+=1
print(cnt)
    
N = int(input())
dasom = int(input())
cnt = 0
n_list = []

for i in range(N-1):
    n_list.append(int(input()))
n_list.sort(reverse=True)

if N == 1:
    print(0)
else:
    while n_list[0] >= dasom:
        dasom+=1
        n_list[0]-=1
        cnt+=1
        n_list.sort(reverse = True)
    print(cnt)
H, M, S = map(int, input().split())
T = int(input())

S+=T
M+=S//60
H+=M//60

print(H%24, M%60, S%60)
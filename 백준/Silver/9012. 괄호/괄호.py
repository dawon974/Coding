import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    str = input()
    stack = []
    for j in str:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                stack.append(j)
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
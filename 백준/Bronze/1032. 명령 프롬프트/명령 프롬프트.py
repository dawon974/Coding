n=int(input())
w=list(input())

for _ in range(n-1):
    w2=input()
    for i in range(len(w)):
        if w[i] != w2[i]:
            w[i] = '?'
        else:
            continue
print(*w, sep="")
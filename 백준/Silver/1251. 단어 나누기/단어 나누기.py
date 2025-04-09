w=input()
result=[]

for i in range(1, len(w)):
    for j in range(i+1, len(w)):
        case1 = w[:i][::-1]
        case2 = w[i:j][::-1]
        case3 = w[j:][::-1]
        result.append(case1 + case2 + case3)
print(sorted(result)[0])
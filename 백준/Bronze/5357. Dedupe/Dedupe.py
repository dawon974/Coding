n=int(input())
result=[]

for _ in range(n):
    s = input()
    result = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            result+=s[i]
    print(result)
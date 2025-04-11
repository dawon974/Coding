N = int(input())
#처음에 모두 그룹 단어라고 가정
cnt=N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt-=1
            break
print(cnt)
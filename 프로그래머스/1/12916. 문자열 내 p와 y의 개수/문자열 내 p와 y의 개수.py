def solution(s):
    answer = True
    p1=0
    y1=0
    s=s.lower()
    for i in s:
        if i=="p":
            p1+=1
        elif i=="y":
            y1+=1
    if p1==y1:
        return answer
    else:
        return False
while 1:
    N = input()
    if N == '0':
        break
    sum = len(N)+1
    for i in N:
        if i == '0':
            sum+=4
        elif i == '1':
            sum+=2
        else:
            sum+=3
    print(sum)
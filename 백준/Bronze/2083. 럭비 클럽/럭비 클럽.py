while True:
    a, b, c = input().split()
    if a == "#" and int(b) == 0 and int(c) == 0:
        break
    elif int(b) > 17 or int(c) >= 80:
        print(f"{a} Senior")
    else:
        print(f"{a} Junior")
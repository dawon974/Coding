while True:
    n = float(input())
    if n == 0:
        break
    else:
        total = 1+n+(n**2)+(n**3)+(n**4)
        print(f"{total:.2f}")
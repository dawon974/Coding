for _ in range(int(input())):
  n=int(input())
  for i in [25, 10, 5, 1]:
    print(n//i, end=' ')
    n=n%i
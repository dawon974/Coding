dial=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

ret=0
n=input()

for i in range(len(n)):
  for j in dial:
    if n[i] in j:
      ret+=dial.index(j)+3

print(ret)
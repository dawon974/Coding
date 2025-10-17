number = set(range(1,10001))
number_set = set()

for num in number:
    for j in str(num):
        num+=int(j)
    number_set.add(num)

self_number = number - number_set
for i in sorted(self_number):
        print(i)
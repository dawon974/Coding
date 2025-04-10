N = int(input())
beard=[]

for _ in range(N):
    beard.append(list(map(int, input().split())))
    
print("Gnomes:")
for i in beard:
    if i == sorted(i) or i == sorted(i, reverse=True):
        print("Ordered")
    else:
        print("Unordered")
        
    
    
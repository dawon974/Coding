n = int(input())
nums=[]
num = list(map(int, input().split()))

result = 0

if n==1:
    print(sum(num)-max(num))
else:
    nums.append(min(num[0], num[5]))
    nums.append(min(num[1], num[4]))
    nums.append(min(num[2], num[3]))
    
    nums.sort()
    
    n1=(n-2)*(n-2) + (n-1)*(n-2)*4
    n2=(n-2)*4+(n-1)*4
    n3=4

    result = n1*nums[0] + n2*(nums[0]+nums[1]) + n3*sum(nums)

    print(result)
N, M = map(int, input().split())
    
package = []
single = []

for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)
p = min(package)
s = min(single)

result = min(N//6 * p + N%6 * s, (N//6 + 1) * p, N * s)
print(result)
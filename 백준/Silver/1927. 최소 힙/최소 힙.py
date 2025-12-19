import sys
import heapq as hp

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    
    if x > 0 :
        hp.heappush(heap, x)
    else:
        if len(heap) >= 1:
            print(hp.heappop(heap))
        else:
            print(0)
        
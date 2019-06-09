import math
n = int(input())
l = list(map(int,input().split()))
i = 1
maxm = 0
for x in range(len(l)):
    maxm = max(maxm,l[x])
    if x+1 > maxm:
        maxm = 0
        i+=1
print(i)
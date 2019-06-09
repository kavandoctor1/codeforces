import math
n = int(input())
l = list(map(int,input().split()))
need = math.ceil(n/2)
zeroes = 0
neg = 0
pos = 0
for i in l:
    if i == 0:
        zeroes+=1
    elif i < 0:
        neg+=1
    else:
        pos+=1
if pos >= need:
    print(1)
elif neg >= need:
    print(-1)
else:
    print(0)
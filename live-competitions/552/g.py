import sys
from math import gcd
n = int(input())
ls = list(map(int,input().split()))
l = list(ls)
l.sort()
firstcut = (l[0]*l[1])//gcd(l[0],l[1])
low = 0
high = n
while low != high:
    mid = (low+high)//2
    if l[mid] < firstcut:
        low = mid+1
    else:
        high = mid
l = l[:(high+2)]
minm = 111000000000000000000000000
curr = []
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        a = ls.index(l[i])
        ls.remove(l[i])
        b = ls.index(l[i])+1
        print(a+1,b+1)
        sys.exit(0)

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        value = l[i]*l[j]//gcd(l[i],l[j])
        if value < minm:
            minm = value
            curr = [l[i],l[j]]
a = ls.index(curr[0])
b = ls.index(curr[1])
print(min(a+1,b+1),max(a+1,b+1))

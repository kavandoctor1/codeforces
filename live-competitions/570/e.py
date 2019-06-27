from itertools import combinations
import sys
n,k = map(int,input().split())
s =  input()
current = len(s)
cost = 0
while k > 0:
    if current <0:
        print(-1)
        sys.exit()
    x = len(set(combinations(s,current)))
    if k < x:
        cost+=k*(len(s)-current)
        break
    else:
        cost+= x*(len(s)-current)
        k-=x
    current -=1
print(cost)

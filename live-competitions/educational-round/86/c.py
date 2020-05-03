import math
def num(a,b,x):
    l = a*b//math.gcd(a,b)
    k = l - max(a,b)
    k*= (x//l)
    n = x - x//l * l - max(a,b) + 1
    if (n > 0):
        k += n
    
    return k
    
for _ in range(int(input())):
    a,b,q = map(int,input().split())
    ans = []
    for _ in range(q):
        li, ri = map(int,input().split())
        n = num(a,b,ri) - num(a,b,li-1)
        ans.append(str(n))
    print(" ".join(ans))
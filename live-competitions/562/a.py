n,a,x,b,y = map(int,input().split())
bl = False
while True:
    a+=1
    if a > n:
        a-=n
    b-=1
    if b < 1:
        b+=n
    if a == b:
        bl = True
        break
    if a == x or b == y:
        break
if bl:
    print("YES")
else:
    print("NO")
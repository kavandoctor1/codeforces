import sys
x,y,z = map(int,input().split())
a,b,c = map(int,input().split())
if a < x:
    print("NO")
    sys.exit()
if a+b+c < x+y+z:
    print("NO")
    sys.exit()
a-=x
if a+b <y:
    print("NO")
    sys.exit()
print("YES")
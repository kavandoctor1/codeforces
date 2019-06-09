import sys
a,b = map(int,input().split())
if a > b:
    a,b = b,a
if b%a == 0:
    print(0)
    sys.exit()
x = abs(b-a)
print((x - a%x)%x)
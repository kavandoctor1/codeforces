n = int(input())
for _ in range(n):
    n,a,b = map(int,input().split())
    if 2*a <= b:
        print(a*n)
    else:
        print(a*(n%2)+b*(n//2))
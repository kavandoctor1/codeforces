for _ in range(int(input())):
    a,b,k = map(int,input().split())
    n = (a-b)*(k//2)
    if k%2:
        n+=a
    print(n)
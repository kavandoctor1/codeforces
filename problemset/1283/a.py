for _ in range(int(input())):
    h,m = map(int,input().split())
    print(60*(23-h) + (60 - m))
for _ in range(int(input())):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    if (2*a <= b):
        print((abs(x) +abs(y)) * a)
    else:
        print(abs(x-y)*a + b*(min(abs(x), abs(y))))
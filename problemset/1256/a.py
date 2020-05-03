for _ in range(int(input())):
    a,b,n,S = map(int,input().split())

    S -= n*min(S//n,a)
    if S <= b:
        print("YES")    
    else:
        print("NO")
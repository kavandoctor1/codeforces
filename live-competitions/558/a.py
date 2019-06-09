n,m = map(int,input().split())
best = n//2
if m > best:
    if n%2:
        print(2*best - m +1)
    else:
        print(2*best - m)
else:
    print(max(m,1))
n,b,a = map(int,input().split())
chg = [a,b]
road = list(map(int,input().split()))
i = 0
while i < n:
    if chg[0] == 0 and chg[1] == 0:
        break
    if road[i] != 1:
        if chg[0] == 0:
            chg[1]-=1
        else:
            chg[0] -= 1
    else:
        if chg[0] == a:
            chg[0] -= 1
    print(i,chg)
    i+=1
print(i)

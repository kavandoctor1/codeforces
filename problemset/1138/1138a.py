n = int(input())
l = map(int,input().split())
ls = [[a,1] for a in l]
i = 0
while i < len(ls)-1:
    if ls[i][0] == ls[i+1][0]:
        ls[i+1][1] += ls[i][1]
        ls.pop(i)
    else:
        i+=1
if len(ls) == 1:
    print(0)
else:
    maxm = 0
    for i in range(len(ls)-1):
        maxm = max(maxm,min(ls[i][1],ls[i+1][1]))
    print(maxm*2)
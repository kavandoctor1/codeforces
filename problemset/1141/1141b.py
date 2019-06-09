n = int(input())
l = list(map(int,input().split()))
l = l+l
maxm = 0
x = 0
for i in l:
    if i == 1:
        x+=1
    else:
        maxm = max(maxm,x)
        x = 0
maxm = max(maxm,x)
print(maxm)
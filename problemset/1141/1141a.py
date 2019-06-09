n,m = map(int,input().split())
dif = m/n
i = 0
while dif%2 == 0:
    dif /=2
    i+=1
while dif%3 == 0:
    dif/=3
    i+=1
if dif != 1:
    print(-1)
else:
    print(i)
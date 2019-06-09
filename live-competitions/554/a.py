n,m = map(int,input().split())
i = list(map(int,input().split()))
j = list(map(int,input().split()))
oddi = 0
eveni = 0
for x in i:
    if x%2 == 1:
        oddi+=1
    else:
        eveni+=1
oddj = 0
evenj = 0
for x in j:
    if x%2 == 0:
        evenj+=1
    else:
        oddj+=1
print(min(oddj,eveni)+min(evenj,oddi))
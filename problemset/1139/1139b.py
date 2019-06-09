n = int(input())
l = list(map(int,input().split()))
l.reverse()
f = l[0]
maxm = l[0]
for i in range(1,n):
    a = max(0,min(maxm-1,l[i]))
    maxm = min(maxm,a)
    f += a
print(f)
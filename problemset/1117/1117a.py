n = int(input())
l = list(map(int,input().split()))
prefix = [0]
for i in l:
    prefix.append(prefix[-1]+i)
prefix.pop(0)
maxm = 0
length = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        s = (prefix[j-1]-prefix[i-1])/(j-i)
        if s > maxm:
            maxm = max(maxm,s)
            length = j-i
        if s == maxm:
            length = max(length,j-i)
print(length)
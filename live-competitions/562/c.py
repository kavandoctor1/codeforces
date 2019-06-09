n,m = map(int,input().split())
l = [0]+list(map(int,input().split()))
i = 1
steps = 0
while i < n:
    if l[i] > l[i+1]:
        a = m-l[i] + l[i-1]
        b = l[i] - l[i+1]
        steps = max(steps,min(a,b))
    i+=1
print(steps)
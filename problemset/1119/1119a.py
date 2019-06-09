n = int(input())
l = list(map(int,input().split()))
i = 0
while i <n:
    if l[i] != l[-1]:
        break
    i+=1
a = n-i-1
j = 1
while j <= n:
    if l[j*-1] != l[0]:
        break
    j+=1
print(max(a,n-j))

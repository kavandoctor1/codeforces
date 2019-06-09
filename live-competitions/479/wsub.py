n,k = map(int, input().split())
while k > 0:
    ldig = n%10
    if ldig == 0:
        n= n//10
        k-=1
        continue
    if k <= ldig:
        n-=k
        break
    k-=(ldig+1)
    n = n//10
print(n)
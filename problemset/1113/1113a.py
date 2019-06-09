n,v = map(int,input().split())
num = max(n-v,0)
fuel = min(v,n) + int((num)*(num+1)//2)-1
print(fuel)
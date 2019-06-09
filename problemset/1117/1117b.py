n,m,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
x = m//(k+1)
a = x*(l[-1]*k+l[-2])
y = m%(k+1)
a+=y*l[-1]
print(a)
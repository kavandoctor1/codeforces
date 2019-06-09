n = int(input())
l = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
l.sort()
l.reverse()
tot = sum(l)
for i in c:
    print(tot-l[i-1])
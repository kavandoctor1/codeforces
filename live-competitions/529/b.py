n = int(input())
l = list(map(int,input().split()))
l.sort()
cur = l[-1] - l[0]
print(cur-max(l[1]-l[0], l[-1]- l[-2]))
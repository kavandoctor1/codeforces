n = int(input())
l = list(set(map(int,input().split())))
l.sort()
if len(l) == 1:
    ans = 0
elif len(l) == 2:
    if (l[0] + l[1])%2 == 0:
        ans = abs(l[0]-l[1])//2
    else:
        ans = abs(l[1]-l[0])
elif len(l) == 3:
    if l[2] - l[1] == l[1] - l[0]:
        ans = abs(l[2] - l[1])
    else:
        ans = -1
else:
    ans = -1

if ans >= 0:
    print(ans)
else:
    print(-1)

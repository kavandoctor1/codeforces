n,k = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
if n == k:
    ans = ls[-1]
elif k == 0 and ls[0] >1:
    ans = ls[0]-1
elif k == 0:
    ans = -1
elif n == 1 and k == 1:
    ans = ls[0]
elif ls[k] == ls[k-1]:
    ans = -1
else:
    ans =ls[k-1]

if ans >0 and ans <= pow(10,9):
    print(ans)
else:
    print(-1)
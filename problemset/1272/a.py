# for _ in range(int(input())):
#     l = list(map(int,input().split()))
#     l.sort()
#     if(l[0] < l[2]):
#         l[0] += 1
#     if(l[1] < l[2]):
#         l[1] += 1
#     elif l[1] > l[0]:
#         l[1] -=1
#     if l[2] > l[0]:
#         l[2] -=1
#     print(abs(l[1] - l[0]) + abs(l[2] - l[1]) + abs(l[2] - l[0]))

import math
def findDifference(a):
    return abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[0] - a[2])
for _ in range(int(input())):
    l = list(map(int, input().split()))
    q = [-1,0,1]
    a = [findDifference([l[0] + a, l[1] + b, l[2] + c]) for a in q for b in q for c in q]
    print(min(a))
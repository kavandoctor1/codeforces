import sys
from collections import Counter
al = int(input())
b = list(map(int,input().split()))
c =list(map(int,input().split()))
for i in range(len(b)):
    if b[i] > c[i]:
        print(-1)
        sys.exit()
a = []
alt = None
full = Counter(b+c)
for key in full:
    if full[key] %2:
        if full[key] == 1:
            a.append(key)
            break
        else:
            alt = key
if len(a) == 0:
    if alt:
        a.append(alt)
    else:
        a.append(b[0])
while len(a) < al:
    try:
        try:
            ind = b.index(a[-1])
            impo = "b"
        except:
            ind = c.index(a[-1])
            impo = "c"
    except:
        print(-1)
        sys.exit()
    if impo == "b":
        a.append(c[ind])
    else:
        a.append(b[ind])
    b.pop(ind)
    c.pop(ind)
print(" ".join(map(str,a)))

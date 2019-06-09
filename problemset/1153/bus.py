import math
nr, at = map(int,input().split())
ls = []
for _ in range(nr):
    st, inter = map(int,input().split())
    if st >= at:
        ls.append(st)
        continue
    space = math.ceil((at-st)/inter)
    st += (space*inter)
    ls.append(st)
print(ls.index(min(ls))+1)
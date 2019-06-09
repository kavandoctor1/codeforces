n = int(input())
l = sorted(list(map(int,input().split())))
i = 0
while len(l) > 0 and i < n:
    j = 0
    bl = True
    while j < len(l):
        if l[j] >= i+1:
            l = l[j+1:]
            bl = False
            break
        j+=1
    if bl:
        break
    i+=1
    if len(l) == 0:
        break
print(i)
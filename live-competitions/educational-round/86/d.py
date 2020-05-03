n,k = map(int,input().split())
m = list(map(int,input().split()))
c = list(map(int,input().split()))
length = []
t = []
m.sort()
m.reverse()
for M in m:
    cap = c[M-1]
    put = False
    for i in range(len(t)):
        if(length[i] < cap):
            put = True
            t[i].append(M)
            length[i] += 1
            break
    if not put:
        t.append([M])
        length.append(1)
print(len(t))
for test in t:
    print(" ".join(map(str,[len(test)] + test)))
    

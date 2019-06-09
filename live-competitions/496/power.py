input()
s = list(map(int,input().split()))
connect = []
for i in range(31):
    p = pow(2,i)
    for a in s:
        if a == p-a:
            if s.count(a) == 1:
                continue
        if (p - a) in s:
            connect.append(a)
            connect.append(p-a)

delete = 0
for i in s:
    if not i in connect:
        delete += 1
print(delete)

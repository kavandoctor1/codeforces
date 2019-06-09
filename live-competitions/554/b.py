import sys
def add(b):
    if b[-1] == 0:
        b[-1] = 1
        return b
    elif len(b) == 1:
        return [1,0]
    else:
        return add(b[:len(b)-1])+[0]
n = int(input())
bb = bin(n)[2:]
b = [int(c) for c in bb]
if all(c for c in b):
    print(0)
    sys.exit()
l = len(b)
num = 0
steps = []
while True:
    n = b.index(0)
    for i in range(n,l):
        if b[i] == 0:
            b[i] = 1
        else:
            b[i] = 0
    steps.append(l-n)
    num+=1
    if all(c for c in b):
        break
    b = add(b)
    num+=1
    if all(c for c in b):
        break
print(num)
print(" ".join(map(str,steps)))
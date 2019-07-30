from sys import exit
n,i = map(int,input().split())
l = sorted(list(map(int,input().split())))
k = (i*8)//n
K = 2**k
diff = len(set(l))- K
if diff <= 0:
    print(0)
    exit()
minm = 10000000000000000
for left in range(l[diff]+1):
    for r in range(l[-1]+1):
        if(left>r):
            continue
        size = 0
        change = 0
        for i in l:
            if i >left and i <r:
                size+=1
            elif i != left and i !=r:
                change+=1
        size+=2
        if(size<=K):
            minm = min(change,minm)
print(minm)
            
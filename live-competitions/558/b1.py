from collections import Counter
import sys
n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    ls = sorted(list(Counter((Counter(l[:n-i]).values())).items()))
    if len(ls) == 1 and ls[0][0] == 1:
        print(n-i)
        sys.exit()
    elif len(ls) == 2:
        if (ls[1][0]-ls[0][0] == 1 and ls[1][1] == 1)or (1,1) in ls:
            print(n-i)
            sys.exit()
print(0)        
    

    
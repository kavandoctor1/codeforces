def possible(ar):
    m = min(ar)
    x = ar.index(m)
    if(ar[-1] == m):
        i = 0
        while len(ar) > 0 and ar[-1] == m+i:
            ar.pop()
            i+=1
        if(len(ar) == 0):
            return True
        m = min(ar)
        x = ar.index(m)
        
    if not all(ar[i] == ar[i-1] + 1 for i in range(x+1, len(ar))):
        return False
    else:
        if(x == 0):
            return True
        return possible(ar[:x])



for _ in range(int(input())):
    N = int(input())
    ar = list(map(int,input().split()))
    if(possible(ar)):
        print("Yes")
    else:
        print("No")
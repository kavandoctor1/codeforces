import sys
n = int(input())
l = list(map(int,input().split()))
points = 0
for i in range(n-1):
    if l[i] == 1:
        if l[i+1] == 2:
            points+=3
        else:
            points+=4
        
        
    elif l[i] == 2:
        if l[i+1] == 1:
            points+=3
        else:
            print("Infinite")
            sys.exit()
    else:
        if l[i+1] == 1:
            points+=4
            if i+2 < n and l[i+2] == 2:
                points-=1
        else:
            print("Infinite")
            sys.exit()            
print("Finite")
print(points)
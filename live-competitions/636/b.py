for _ in range(int(input())):
    n = int(input())
    if(n%4 == 0):
        a = [2*x for x in range(1,n//2+1)]
        b = [2*x + 1 for x in range(1,n//2 + 1)]
        for i in range(n//4):
            b[i] -= 2
        ar = a+b
        print("YES")
        print(" ".join(list(map(str,ar))))
    else:
        print("NO")
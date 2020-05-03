for _ in range(int(input())):
    N = int(input())
    ar = list(map(int,input().split()))
    arr = []
    curr = []
    sign = 1 if ar[0]>= 0 else -1
    for item in ar:
        if(item//abs(item) == sign):
            curr.append(item)
        else:
            arr.append(curr)
            sign*=-1
            curr = [item]
    arr.append(curr)
    ans = 0
    a = sum([max(l) for l in arr])
    print(a)
            
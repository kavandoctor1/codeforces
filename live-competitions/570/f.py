from itertools import combinations
for _ in range(int(input())):
    input()
    ls = list(map(int,input().split()))
    tres = combinations(ls,3)
    print(max(tres, ke))
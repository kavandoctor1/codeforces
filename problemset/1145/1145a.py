def ar(n):
    if len(n) == 1:
        return 1
    if sorted(n) == n:
        return len(n)
    b = len(n)//2
    return max(ar(n[:b]),ar(n[b:]))
n = int(input())
l = list(map(int,input().split()))
print(ar(l))
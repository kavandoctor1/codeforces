n = int(input())
l = list(map(int,input().split()))
fet = l[-1]
while l[-1] == fet:
    l.pop()
print(len(l))
import sys
n = int(input())
l = list(map(int,input().split()))
even = []
odd = []
for i in l:
    if i%2:
        odd.append(i)
    else:
        even.append(i)
if len(even) > len(odd):
    fet = even
else:
    fet = odd
diff = abs(len(even)-len(odd)) -1
if diff < 1:
    print(0)
    sys.exit()
fet.sort()
tot = 0
for i in range(diff):
    tot += fet[i]
print(tot)
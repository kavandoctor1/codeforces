import sys
n = int(input())
l = list(map(int,input().split()))
a = [0 for _ in range(200002)]
for i in range(200001):
    j = l.count(i)
    if j > 2:
        print("NO")
        sys.exit()
    a[i] = j
print("YES")
print(a.count(2))
for i in range(200001):
    if a[i] == 2:
        print(i,end=" ")
        a[i]-=1
print()
print(a.count(1))
for i in range(200000,-1,-1):
    if a[i] == 1:
        print(i,end=" ")
print()
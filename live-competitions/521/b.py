import sys
n = int(input())
s = list(map(int,input().split()))
disturb = []
for i in range(1,n-1):
    if s[i-1] and s[i+1] and (not s[i]):
        disturb.append(i)
if len(disturb) == 0:
    print(0)
    sys.exit(0)
count = 0
while len(disturb) > 0:
    if len(disturb) == 1:
        count += 1
        break
    if disturb[0] +2 == disturb[1]:
        disturb.pop(0)
        disturb.pop(0)
        count += 1
    else:
        disturb.pop(0)
        count += 1
print(count)

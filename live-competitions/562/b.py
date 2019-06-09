from sys import exit
from collections import Counter
n,m = map(int,input().split())
pairs = []
tot = []
for _ in range(m):
    a,b = map(int,input().split())
    tot.append(a)
    tot.append(b)
    pairs.append([min(a,b), max(a,b)])
tot = Counter(tot).most_common()
for i in range(len(tot)-1):
    if tot[i][1] + tot[i+1][1] < m:
        break
    for j in range(i+1,len(tot)):
        if tot[i][1] + tot[j][1] - pairs.count([min(tot[i][0], tot[j][0]), max(tot[i][0], tot[j][0])]) == m:
            print("YES")
            exit()
print("NO")
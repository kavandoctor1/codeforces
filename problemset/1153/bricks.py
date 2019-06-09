n,m,h = map(int,input().split())
front = list(map(int,input().split()))
side = list(map(int,input().split()))
rows = []
for _  in range(n):
    rows.append(input().split())
for i in range(n):
    if rows[i].count('1') == 1:
        for j in range(m):
            if rows[i][j] == '1':
                rows[i][j] = side[i]
            elif rows[i][j] == '0':
                rows[i][j] = 0
    elif rows[i].count('0') == m:
        for j in range(m):
            rows[i][j] = 0
for a in range(m):
    ls = []
    for b in range(n):
        ls.append(rows[b][a])
    if ls.count('1') == 1 and ls.count('0') == n-1:
        for b in range(n):
            if rows[b][a] == '1':
                rows[b][a] = front[a]
            elif rows[b][a] == '0':
                rows[b][a] = 0
    if all(item == 0 or item == '0' for item in ls):
        for j in range(n):
            rows[j][a] = 0

for i in range(n):
    if rows[i].count('1') > 1:
        minm = 100000000
        current = []
        for x in range(m):
            if rows[i][x] == '1':
                if front[x] >= side[i]:
                    if front[x] < minm:
                        minm = front[x]
                        current = [x]
                    elif front[x] == minm:
                        current.append(x)
        for c in current:
            rows[i][c] = side[i]

for a in range(m):
    ls = []
    for b in range(n):
        ls.append(rows[b][a])
    maxm = 10000
    current = []
    if ls.count('1') > 1:
        for b in range(n):
            if rows[b][a] == '1':
                if side[b] >= front[a]:
                    if side[b] < maxm:
                        maxm = side[b]
                        current = [b]
                    elif side[b] == maxm:
                        current.append(b)
        for c in current:
            rows[c][a] = front[a]


for row in rows:
    for i in row:
        print(i, end = " ")
    print()


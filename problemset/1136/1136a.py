chap = int(input())
ls = []
for _ in range(chap):
    ls.append(list(map(int,input().split())))
ind = int(input())
i = 0
while i < chap:
    if ls[i][1] >= ind:
        break
    i+=1
print(chap-i)
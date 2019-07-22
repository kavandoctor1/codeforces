from sys import exit
n = int(input())
ls = list(map(int,input().split()))
x= ls.index(max(ls))
for i in range(x):
    if ls[i]>= ls[i+1]:
        print("NO")
        exit()
for i in range(x,len(ls)-1):
    if ls[i]<= ls[i+1]:
        print("NO")
        exit()
print("YES")
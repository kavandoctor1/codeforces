input()
s = input().split()
ls = []
l = []
for i in s:
    if i == '1':
        ls.append(l)
        l = []
    else:
        l.append(i)
ls.append(l)
ls.pop(0)
print(len(ls))
for i in ls:
    print(len(i) + 1, end = " ")
print()

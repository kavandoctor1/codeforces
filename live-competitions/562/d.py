s = input()
n = len(s)
lr = []
for x in range(n):
    for k in range(1,(n-x-1)//2 + 1):
        if s[x] == s[x+k] and s[x+k] == s[x+2*k]:
            for i in range(x+1):
                for j in range(x+2*k, n):
                    lr.append(str(i)+str(j))
print(len(set(lr)))
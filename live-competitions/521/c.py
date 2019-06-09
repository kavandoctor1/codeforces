n = int(input())
s = list(map(int,input().split()))
tot = sum(s)
ls = []
for i in range(1,n+1):
    if (tot - s[i-1])/2 in s:
        if (tot - s[i-1])/2 == s[i-1]:
            if s.count(s[i-1]) > 1:
                ls.append(i)
        else:
            ls.append(i)
print(len(ls))
print(" ".join(map(str,ls)))
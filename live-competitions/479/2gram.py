from collections import Counter
input()
s = input()
l = []
for c in range(len(s)-1):
    l.append(s[c:c+2])
x = Counter(l).most_common(1)
print(x[0][0])
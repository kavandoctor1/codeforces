def regular(s,j):
    if s[j] == "(":
        c = ")"
    else:
        c = "("
    s = s[:j]+c+s[j+1:]
    i = 0
    for c in s:
        if c == "(":
            i+=1
        else:
            i-=1
        if i < 0:
            return False
    if i!= 0:
        return False
    return True

n = int(input())
s = input()
prefix = [0]
for c in s:
    if c == "(":
        prefix.append(prefix[-1]+1)
    else:
        prefix.append(prefix[-1]-1)
prefix.pop(0)
print(prefix)
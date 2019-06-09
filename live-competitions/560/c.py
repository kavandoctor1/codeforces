n = int(input())
s = [c for c in input()]
t = ""
i = 0
while i < len(s) -1:
    if i%2==0 and s[i] == s[i+1]:
        s.pop(i)
    else:
        i+=1
if len(s)%2:
    s.pop()
print(n-len(s))
print("".join(s))
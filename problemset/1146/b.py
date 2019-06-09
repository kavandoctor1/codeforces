import sys
s = input()
for i in range(len(s)):
    cut = s[len(s)-i:]
    remain = s[:len(s)-i]
    r = ""
    for c in remain:
        if c!= "a":
            r+=c
    if r == cut:
        print(remain)
        sys.exit()
print(":(")
n = int(input())
s = input()
if "".join(sorted(s)) == s:
    print("NO")
else:
    print("YES")
    for i in range(len(s)-1):
        if ord(s[i+1]) < ord(s[i]):
            print(i+1,i+2)
            break
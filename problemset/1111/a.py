import sys
s = input()
t = input()
vowels = "aeiou"
consos = "bcdfghjklmnpqrstvwxyz"
if len(s) == len(t):
    for i in range(len(s)):
        if s[i] in vowels and t[i] in vowels or s[i] in consos and t[i] in consos:
            continue
        else:
            print("No")
            sys.exit()
    print("Yes")
else:
    print("No")
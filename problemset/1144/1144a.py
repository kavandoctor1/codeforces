def diverse(s):
    if len(s) == 1 or len(s) == 0:
        return True

    s = [c for c in s]
    s.sort()
    if not all(abs(ord(s[i])-ord(s[i+1])) == 1 for i in range(len(s)-1)):
        return False
    return True


for _ in range(int(input())):
    if diverse(input()):
        print("Yes")
    else:
        print("No")
for _ in range(int(input())):
    s = input()
    if(all(s[i] == s[i+1] for i in range(len(s)-1))):
        print(s)
    else:
        t = list(s)
        if(s[0] == "1"):
            print("10"*len(t))
        else:
            print("01"*len(t))
import math
n = int(input())
s = input()
c = int((math.sqrt(1 + 8*n)-1)//2)
for i in range(1,c+1):
    print(s[0],end = "")
    s = s[i:]
print()
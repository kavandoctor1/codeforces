n = int(input())
s = input()
part = s[:n-10]
t = (n-11)//2
if t >= part.count('8'):
    print("NO")
else:
    print("YES")
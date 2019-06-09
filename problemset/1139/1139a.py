n = int(input())
s = input()
tot = 0
for i in range(n):
    if int(s[i])%2==0:
        tot+=i+1
print(tot)
n,x,y = map(int,input().split())
s = input()[::-1]
count = s[:y].count('1')
if s[y] == "0":
    count+=1
count += s[y+1:x].count('1')
print(count)

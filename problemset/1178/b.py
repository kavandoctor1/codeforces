from sys import exit
s = [c for c in input()]
if len(s)<5:
    print(0)
    exit()
start = 0
while s[0] == 'o' or (s[0] == 'v' and s[1] == 'o'):
    start+=1
    if start >len(s)-4:
        print(0)
        exit()
s=s[start:]
nums = []
current = 0
curl = 'v'
index = 0
for c in s:
    if c == curl:
        current+=1
    else:
        if(not(curl == 'o' and (index+1== len(s) or s[index+1]=='o'))):
            nums.append(current)
            current = 1     
            curl = str(c)
    index+=1
if curl == 'v':
    nums.append(current)
total = 0
for i in range(0,len(nums),2):
    tot=0
    it = 0
    mult = nums[i] -1
    for j in range(i+2,len(nums),2):
        it+=nums[j-1]
        tot+=mult*it*(nums[j]-1)
    total+=tot
print(total)
        

n = int(input())
big = input()
if(n%2):
    x=n//2
    y=x+1
    z=int(x)+1
    while big[x] == '0' and x<n-1:
        x+=1
    while big[y]=="0"and x<n-1:
        y+=1
    while big[z] == '0'and z>1:
        z-=1
    a=int(big[:x])
    b = int(big[x:])
    a2=int(big[:y])
    b2 = int(big[y:])
    a3=int(big[:z])
    b3 = int(big[z:])
    print(min(a+b,a2+b2,a3+b3))
else:
    x = n//2
    z=n//2+1
    while big[x] == '0' and x < n-1:
        x+=1
    while big[z] == '0'and z>0:
        z-=1
    uno = int(big[:x])
    dos = int(big[x:])
    a3=int(big[:z])
    b3 = int(big[z:])
    print(min(uno+dos,a3+b3))

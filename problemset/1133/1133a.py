h1,m1 = map(int,input().split(":"))
h2,m2= map(int,input().split(":"))
mint = (h2-h1)*60+(m2-m1)
mint= mint//2
hr = mint//60
min = mint%60
h1+=hr
m1+=min
if m1 >= 60:
    h1+=1
    m1-=60
h1,m1 = str(h1),str(m1)
print("0"*(2-len(h1))+h1+":"+"0"*(2-len(m1))+str(m1))
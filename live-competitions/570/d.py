for _ in range(int(input())):
    input()
    box = {}
    candy = list(map(int,input().split()))
    for c in candy:
        try:
            box[c]+=1
        except:
            box[c] = 1
    ls = list((box.values()))
    ls.sort(reverse=True)
    i = 0
    sum = 0
    current = ls[0]+1
    while i < len(ls):
        if current == 1:
            break
        if ls[i] >= current:
            sum+=current-1
            current -= 1
        else:
            sum+=ls[i]
            current = ls[i]
        i+=1
    print(sum)
    
    
    
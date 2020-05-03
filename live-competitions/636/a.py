for _ in range(int(input())):
    N = int(input())
    k = 2
    while True:
        if(N%(pow(2,k)-1) == 0):
            print(N//(pow(2,k)-1))
            break
        k+=1
        
        
    
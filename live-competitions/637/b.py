for _ in range(int(input())):
    n,k = map(int,input().split())
    mts = list(map(int,input().split()))
    peaks = [0]
    for i in range(1,n-1):
        if(mts[i] > mts[i-1] and mts[i] > mts[i+1]):
            peaks.append(1+peaks[-1])
        else:
            peaks.append(0+peaks[-1])
    peaks.append(peaks[-1])
    maxm = 0
    la = -1
    for l in range(0,n-k+1):
        if(peaks[l+k-2]-peaks[l] + 1 > maxm):
            maxm = peaks[l+k-2] - peaks[l] + 1
            la = int(l+1)
    print(maxm,la)
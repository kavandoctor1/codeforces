for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print("YES" if all(l[i]%2 == l[i+1]%2 for i in range(n-1)) else "NO")
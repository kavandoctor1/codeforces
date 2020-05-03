dp = dict()
digits = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
def maxd(board, k):
    if((len(board), k) in dp):
        return dp[len(board), k]
    if(len(board) == 0):
        if(k == 0):
            return ""
        else:
            return None
    
    s = board.pop(0)
    for i in range(9,-1, -1):
        if(all((digits[i][j] == s[j] or digits[i][j] == '1') for j in range(7))):
            used = 0
            for j in range(7):
                if(digits[i][j] == '1' and s[j] == '0'):
                    used += 1
            if(used <= k):
                ft = maxd(list(board),k-used)
                dp[len(board), k-used] = ft
                if(ft != None):
                    return str(i) + ft
    return None

n, k = map(int,input().split())

board = [input() for _ in range(n)]
n = maxd(board,k)
if(n == None):
    print(-1)
else:
    print(n)


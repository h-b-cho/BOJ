import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0]*(M+1)
    if M==1:
        print(1)
    elif M==2:
        print(2)
    else:
        dp[0] = 1
        for c in coins:
            for m in range(c, M+1):
                dp[m] += dp[m - c] # dp[k]는 k원을 만드는 경우의 수.
        print(dp[-1])
num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    start = 0
    for _ in range(n):
        dp.append(array[start:start+m])
        start += m

    for y in range(1, m):
        for x in range(n):
            # 왼쪽 위
            if x == 0:
                left_up = 0
            else:
                left_up = dp[x-1][y-1]

            # 왼쪽 아래
            if x == n-1:
                left_down = 0
            else:
                left_down = dp[x+1][y-1]

            #왼쪽
            left_left = dp[x][y-1]

            dp[x][y] = max(left_up, left_left, left_down)+dp[x][y]
    
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
        
    print(result)

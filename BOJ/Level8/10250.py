T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    Y = N % H
    X = N // H + 1
    if Y == 0 :
        Y = H
        X = N // H
    print(Y*100 + X)

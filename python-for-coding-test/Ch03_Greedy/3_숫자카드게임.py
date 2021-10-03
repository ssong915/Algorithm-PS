n,m = map(int, input().split())
min_m = 0
ans = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    min_m = min(arr)
    # if min_m > ans :
    #     ans = min_m
    ans = max(ans, min_m)

print(ans)
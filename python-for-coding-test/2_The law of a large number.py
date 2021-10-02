N,M,K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

first = arr[0]
second = arr[1]
ans = 0

while True:
    for i in range(K):
        if M == 0:
            break
        else:
            ans += first
            M -= 1
    if M == 0:
        break
    else:
        ans += second
        M -= 1

print(ans)

N,M,K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

first = arr[0]
second = arr[1]
ans = 0

group = first*K + second

ans += ( M // (K+1)) * group
ans += ( M % (K+1)) * second

print(ans)
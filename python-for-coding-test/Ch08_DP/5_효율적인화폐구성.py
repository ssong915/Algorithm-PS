n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

num = [10001] * m
for i in range(n):
    for j in range(array[i], m+1):
        if num[j-array[i]] != 10001:
            num[j] = min(num[j-array[i]]+1, num[j])
if num[m] == 10001:
    print(-1)
else:
    print(num[m])

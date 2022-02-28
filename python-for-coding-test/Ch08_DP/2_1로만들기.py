n = int(input())
counter = 0
result = [0]*30001
for i in range(2, n+1):  # 보텀업

    # -1
    result[i] = result[i-1] + 1

    if i % 2 == 0:
        # %2
        result[i] = min(result[i], result[i//2]+1)

    if i % 3 == 0:
        # %3
        result[i] = min(result[i], result[i//3]+1)

    if i % 5 == 0:
        # %5
        result[i] = min(result[i], result[i//5]+1)

print(result[n])

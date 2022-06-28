arr = []

for j in range(10):
    num = int(input())
    mod = num % 42
    arr.append(mod)

arr = set(arr) # set: 중복 제거
print(len(arr))

    
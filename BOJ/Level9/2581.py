M = int(input())
N = int(input())
arr = []

for num in range(M,N+1):
    error = 0
    if num > 1:
        for j in range(2,num):
            if num % j == 0:
                error = 1
                break
        if error == 0:
            arr.append(num)

if len(arr) > 0 :
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
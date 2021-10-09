n,m =  map(int, input().split())
arr = list(map(int, input().split()))
result = 0

arr.sort()

for i in range(n):
    j = i+1
    while j != (n-1) :
        if arr[i] != arr[j]:
            result += ( n-j+1 )
            i += 1
            j += 1
            break
        else:
            j += 1

print(result)
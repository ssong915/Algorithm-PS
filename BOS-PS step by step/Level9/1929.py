M,N = map(int,input().split())
ans = [True]* (N-M+1)
ans[1] = False

for num in range(M,N+1):
    for i in range (2, int(N**0.5)+1):
        if num % i == 0:
            ans[num] = False
            break

for i in range(M,N+1):
    if ans[i]:
        print(i)
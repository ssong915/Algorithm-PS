N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
for i in range(N):
    ans += min(A) * max(B)
    A.remove(min(A))
    B.remove(max(B))

print(ans)


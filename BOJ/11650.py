import operator

N = int(input())
x_y = []

for _ in range(N):
    x,y = map(int,input().split())
    x_y.append([x,y])

x_y.sort(key=lambda x:(x[0],x[1]))

for ans in x_y:
    print(ans[0],ans[1])
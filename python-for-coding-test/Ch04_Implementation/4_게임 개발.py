n, m = map(int, input().split())

x, y, dir = map(int, input().split())
dx =[-1, 0, 1, 0]
dy =[0, 1, 0, -1]

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr[x][y]=1

result  = 0
turnTime = 0

while True:
    dir -= 1 
    if (dir == -1 ):
        dir = 3
    nx = x +dx[dir]
    ny = y +dy[dir]
    if (arr[nx][ny]==0):
        x = nx 
        y = ny
        arr[nx][ny]=1
        result += 1
        turnTime = 0
        continue
    else:
        turnTime +=1 

    if turnTime==4 :
        nx = x-dx[dir]
        ny = y-dy[dir]
        if arr[nx][ny]==1:
            break
        else:
            x = nx
            y = ny
        turnTime = 0

print(result)
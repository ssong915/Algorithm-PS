n = int(input())
board = [[0]*n for _ in range (n)] # empty : 0

k = int(input())
for _ in range (k):
    x,y = map(int,input().split())
    board[x-1][y-1] = 2 # 사과 위치: 2

l = int(input())
times = [0]*10000
for _ in range(l):
    when, dir = input().split()
    times[int(when)] = dir

snake = []
snake.append([0,0])
board[0][0] = 1 # 뱀 위치: 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dir = 1 # 동쪽 바라보고 시작
nx, ny = 0 , 0 # (0,0) 에서 시작

time = 0

while(True):
    time += 1
    nx = nx + dx[dir]
    ny = ny + dy[dir]

    if ( nx<0 or nx>=n or ny<0 or nx>=n or board[nx][ny]==1): # 벽이나, 몸에 닿으면
        break

    if ( board[nx][ny] ==2 ): # 사과 있으면
        snake.append([nx,ny])
        board[nx][ny] = 1
    
    elif ( board[nx][ny] == 0):
        snake.append([nx,ny])
        board[nx][ny] = 1

        delX,delY = snake.pop(0)
        board[delX][delY] = 0

    if ( times[time] == 'D'):
        dir = ( dir+1 )%4
    elif ( times[time] == 'L'):
        dir = ( dir+3 )%4

print(time)
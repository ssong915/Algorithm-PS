n = int(input())
moves = input().split()
x, y = 1,1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(4):
        if move == move_types[i]:
            tempX = x + dx[i]
            tempY = y + dy[i]

    if tempX < 1 or tempY < 1 or tempX > n or tempY > n:
        continue
    # 이동 수행
    x, y = tempX, tempY

print(x, y)
        
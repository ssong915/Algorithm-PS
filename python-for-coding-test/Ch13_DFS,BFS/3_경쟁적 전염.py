from collections import deque

n, k = map(int, input().split())

location = []  # n X n 시험관 상황
virus = []  # 바이러스의 종류와 location이 저장된 리스트
for i in range(n):
    location.append(list(map(int, input().split())))
    for j in range(n):
        if location[i][j] != 0:
            virus.append((location[i][j], i, j, 0))


S, X, Y = map(int, input().split())

virus.sort()  # 첫번째 원소 기준으로 정렬
queue = deque(virus)  # 리스트를 queue로

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while queue:
    virus, x, y, time = queue.popleft()

    if time == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue
        
        if location[nx][ny] == 0:
            location[nx][ny] = virus
            queue.append((location[nx][ny], nx, ny, time+1))

print(location[X-1][Y-1])

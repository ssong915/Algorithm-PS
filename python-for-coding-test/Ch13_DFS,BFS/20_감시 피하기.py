from itertools import combinations

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(str,input().split())))

teachers = []
empty_spaces = []

# 선생님 위치와 빈공간 저장하기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append((i,j))
        if graph[i][j] == 'X':
            empty_spaces.append((i,j))

def monitored():
    for x, y in teachers:
        # 상
        nx, ny = x, y
        while nx > 0:
            nx -= 1
            if graph[nx][ny] == 'S':
                return False

            if graph[nx][ny] == 'O':
                break
        # 하
        nx, ny = x, y
        while nx < N - 1:
            nx += 1
            if graph[nx][ny] == 'S':
                return False
            if graph[nx][ny] == 'O':
                break
        # 좌
        nx, ny = x, y
        while ny > 0:
            ny -= 1
            if graph[nx][ny] == 'S':
                return False
            if graph[nx][ny] == 'O':
                break
        # 우
        nx, ny = x, y
        while ny < N - 1:
            ny += 1
            if graph[nx][ny] == 'S':
                return False
            if graph[nx][ny] == 'O':
                break
    return True


monitor = 0
for walls in combinations(empty_spaces,3):
    # 벽 만들기
    for x,y in walls:
        graph[x][y] = 'O'
    
    if monitored():
        monitor = 1
        print("YES")
        break

    # 벽 없애기
    for x,y in walls:
        graph[x][y] = 'X'

if monitor == 0:
    print("NO")
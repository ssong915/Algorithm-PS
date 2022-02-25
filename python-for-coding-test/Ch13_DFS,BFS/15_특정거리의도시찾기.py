from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

# 방문하지 않은 도시들은 -1로 표기
distance = [-1] * (n+1)
distance[x] = 0
queue = deque()
queue.append(x)

# BFS 수행
while queue:
    v = queue.popleft()
    for node in graph[v]:
        if distance[node] == -1:
            distance[node] = distance[v]+1
            queue.append(node)

# 거리가 k인 도시의 번호들을 출력
check = False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check = True

if check==False:
    print(-1)

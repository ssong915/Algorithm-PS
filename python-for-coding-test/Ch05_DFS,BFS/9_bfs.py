from collections import deque

# 연결 관계 리스트로 표현
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9

def bfs(graph, start, visited):
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque([start])
    # 현재노드 start 노드 방문처리
    visited[start] = True
    # 큐가 빌 때까지
    while queue:
        # 하나씩 pop 후 출력
        v = queue.popleft()
        print(v, end="")
        # pop 된 넘의 이웃한 것들 추가
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)

# bfs
# 큐 구조
# dfs 보다 수행시간이 빠름

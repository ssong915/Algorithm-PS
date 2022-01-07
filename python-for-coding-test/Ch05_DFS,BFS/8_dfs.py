# 연결 관계 리스트로 표현
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 방문 여부를 나타내는 리스트
visited = [False] * 9

# dfs 
def dfs(graph, v, vistited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)

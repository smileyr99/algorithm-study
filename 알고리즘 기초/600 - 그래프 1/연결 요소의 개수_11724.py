import sys
sys.setrecursionlimit(10000)  # 재귀 제한 풀기

def dfs(v):
    visited[v] = True
    for e in range(1, n + 1):
        if not visited[e] and graph[v][e] == 1:
            dfs(e)


n, m = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]   # 0으로 채워진 빈 그래프 생성
visited = [False] * (n + 1)     # 방문한 정점 체크
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1   # 연결된 노드 다 돌고 dfs 빠져나올때 카운트 1 증가

print(cnt)

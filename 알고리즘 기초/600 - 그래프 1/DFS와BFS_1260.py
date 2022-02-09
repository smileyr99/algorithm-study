import sys
from collections import deque


def bfs(v):
    q = deque()  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용
    q.append(v)
    visited2[v] = 1  # 해당 V값 방문처리
    while q:  # q가 빌때까지 돈다
        v = q.popleft()  # 큐에 있는 첫번째 값 꺼냄
        print(v, end=" ")  # 해당 값 출력
        for i in range(1, n + 1): # 1부터 N까지 돈다
            if visited2[i] == 0 and graph[v][i] == 1:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)  # 그 i 값을 추가
                visited2[i] = 1 # i 값을 방문처리


def dfs(v):
    visited1[v] = 1 # 해당 V값 방문처리
    print(v, end=" ")
    for i in range(1, n + 1):
        if visited1[i] == 0 and graph[v][i] == 1: # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)


n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)

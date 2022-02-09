import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    q = deque()
    q.append([a, b])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]  # 행값
            ny = y + dy[i]  # 열값

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 새로운 좌표값을 전의 좌표값에서 +1
                q.append([nx, ny])

    return graph[n - 1][m - 1]


print(bfs(0, 0))
print(*graph)
import sys

n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]  # 방문한 정점 체크리스트

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
flag = False


def cango(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    else:
        return False


def dfs(y, x, py, px, ball):
    if visited[y][x] == 1:  # 방문했으면 True
        return True
    visited[y][x] = True  # 안했을 경우 방문처리

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 바로 이전의 점을 방문할 경우 제외
        # ny==py and nx==px 인 경우를 제외하고 주변의 모든 점을 깊이 우선 순회 가능
        if ny != py or nx != px:
            # 만약 위치를 이동했을때 같은 점의 색이라면
            if cango(ny, nx) and graph[ny][nx] == ball:
                if dfs(ny, nx, y, x, ball):
                    return True
    return False


for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if dfs(i, j, 0, 0, graph[i][j]):
            flag = True
            break

print("Yes") if flag else print("No")

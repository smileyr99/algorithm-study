import sys
from collections import deque


def bfs(a, b):  # 시작점 x,y, 목적지 x,y
    q = deque()
    q.append([a, b])  # 우선 시작점 x,y를 큐에 넣는다.

    while q:
        x, y = q.popleft()

        if x == desx and y == desy:  # 만약 그 x,y가 목적지 x,y라면
            return graph[x][y]  # 목적지(x,y)에 저장되어 있는 값을 리턴

        for i in range(8):
            nx = x + dx[i]  # 행값
            ny = y + dy[i]  # 열값

            if nx >= I or ny >= I or nx < 0 or ny < 0:  # 만약 좌표가 그래프범위를 벗어나면 continue
                continue

            if graph[nx][ny] == 0:  # 만약 점(nx,ny)를 아직 방문하지 않았다면
                graph[nx][ny] = graph[x][y] + 1     # 새로운 점의 값을(이동횟수의 최소값) 전의 값에서 + 1 해준다.
                q.append([nx, ny])


k = int(sys.stdin.readline())
for _ in range(k):
    I = int(input())  # 그래프의 크기 입력
    startx, starty = map(int, input().split())  # 시작점 입력
    desx, desy = map(int, input().split())  # 목적지 입력
    graph = [[0] * I for _ in range(I)]  # 그래프를 I크기 만큼 0으로 초기화

    dx = [-2, -1, 1, 2, -2, -1, 1, 2]  # 행이동좌표
    dy = [1, 2, 2, 1, -1, -2, -2, -1]  # 열이동좌표

    print(bfs(startx, starty))


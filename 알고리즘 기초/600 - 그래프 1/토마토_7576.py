import sys
from collections import deque


# 1들의 좌표값에서 동시에 출발해야하므로 bfs로 큐 이용!!
def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]  # 행값
            ny = y + dy[i]  # 열값

            # 만약 이동한 좌표가 그래프 범위 벗어나면 continue 처리
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            # 만약 위치를 이동했는데 그 좌표값이 0이라면(방문하지 않았다면)
            if graph[nx][ny] == 0:
                q.append([nx, ny])  # 새로운 좌표값을 큐에 추가한 후
                graph[nx][ny] = graph[x][y] + 1  # 새로운 좌표값을 전의 좌표값에서 +1


m, n = map(int, sys.stdin.readline().split())
graph = []
cnt = 0
result = 0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rsplit())))
    cnt += graph[i].count(0)  # 해당그래프를 입력받으면서 0의 개수 세기

# 만약 그래프에 0값이 없다면 모두 익었다는 말이므로 바로 0을 출력 후 종료
if cnt == 0:
    print(0)
    exit()

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()  # 1의 위치를 담을 큐 선언
# 1인 좌표 모두 큐에 넣어주기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

bfs()

cnt = 0  # 0을 셀 cnt값을 0으로 선언
for i in graph:  # bfs를 돈 graph '0'개수 세기
    cnt += i.count(0)
    if cnt > 0:  # 만약 0이 존재한다면
        print(-1)  # -1을 출력하고
        exit()  # 바로 종료

    # 0이 존재하지 않는다면
    result = max(result, max(i))  # 결과값에 그래프의 행마다 최대값을 계속 대입

print(result - 1)  # 시작할 때부터 1로 시작하기 때문에 출력값에 -1을 함

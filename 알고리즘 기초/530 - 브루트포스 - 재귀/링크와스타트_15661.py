import sys

def update():
    sum_team2 = 0
    for i in range(N):
        for j in range(N):
            sum_team2 += arr[i][j]
    return sum_team2


def dfs(depth, n, start, sum_t1, sum_t2):
    global answer
    if depth < N and answer > 0:
        diff = abs(sum_t1 - sum_t2)
        answer = min(answer, diff)

        for i in range(start, N):
            visited[i] = True
            temp_t1 = sum_t1
            temp_t2 = sum_t2
            for j in range(N):
                if i != j:
                    if visited[j]:
                        temp_t1 += arr[i][j] + arr[j][i] # 방문을 했을 경우 팀에 더해준다
                    elif not visited[j]:
                        temp_t2 -= arr[i][j] + arr[j][i] # 만약 2일 경우 (2,3), (2,4)등 이 모든 경우들을 모두 빼준다
            dfs(depth + 1, n, i + 1, temp_t1, temp_t2)
            visited[i] = False


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    answer = int(1e9)

    visited = [False] * N
    # 1명, 2명, …, N//2명 까지만 뽑는 경우의 수
    dfs(0, N // 2, 0, 0, update())

    print(answer)

'''import sys

# 팀의 능력치 합
# def update():
#     global answer
#     sum_team1 = 0
#     sum_team2 = 0
#     for i in range(N):
#         for j in range(N):
#             if visited[i] == visited[j]:
#                 if visited[i]:
#                     sum_team1 += arr[i][j]
#                 else:
#                     sum_team2 += arr[i][j]
#
#     diff = abs(sum_team1 - sum_team2)
#     answer = min(answer, diff)

# 팀의 능력치 합
def update():
    global answer
    sum_team1 = 0
    sum_team2 = 0
    for i in range(N):
        for j in range(N):
            if visited[i] == visited[j]:
                if visited[i]:
                    sum_team1 += arr[i][j]
                else:
                    sum_team2 += arr[i][j]

    diff = abs(sum_team1 - sum_team2)
    answer = min(answer, diff)


def dfs(depth, n, start):
    if depth < N and answer > 0:
        update()

        for i in range(start, N):
            visited[i] = True
            dfs(depth+1, n, i+1)
            visited[i] = False


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    answer = int(1e9)

    visited = [False] * N
    # 1명, 2명, ..., N//2명 까지만 뽑는 경우의 수
    dfs(0, N//2, 0)

    print(answer)'''

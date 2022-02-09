# 팀의 능력치 차이를 계산하는 함수
def update(team1, team2):
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)


def dfs(team1, depth, N, start):
    global answer

    if depth == N//2:  # N // 2 번만큼 재귀를 돌면
        team2 = []
        for i in range(N):
            if i not in team1:  # 스타트팀의 배열에 속하지 않은 사람을 링크팀에 넣음
                team2.append(i)

        diff = update(team1, team2)
        answer = min(answer, diff)
        return

    for i in range(start, N):
        if i not in team1:
            team1.append(i)
            dfs(team1, depth+1, N, i+1)
            team1.pop()

if __name__=="__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = int(1e9)
    dfs([], 0, N, 0)

    print(answer)


'''
def solve(cnt, idx):
    global ans
    if idx == N:
        return
    if cnt == N//2:
        s1, s2 = 0, 0
        for i in range(N):
            for j in range(N):
                if team[i] and team[j]:
                    s1 += scores[i][j]
                if not team[i] and not team[j]:
                    s2 += scores[i][j]
        ans = min(ans, abs(s1-s2))
        return
    team[idx] = True
    solve(cnt+1, idx+1)
    team[idx] = False
    solve(cnt, idx+1)

N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
team = [False]*N
ans = 1e9

solve(0, 0)
print(ans)
'''

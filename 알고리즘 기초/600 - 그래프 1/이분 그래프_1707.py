import sys
sys.setrecursionlimit(1000000)  # 재귀 제한 풀기

input = sys.stdin.readline
K = int(input())


def dfs(V, group):
    visited[V] = group  # 해당 정점의 group 설정(1,-1)

    for i in graph[V]:
        if not visited[i]:  # 만약 방문하지 않았다면
            a = dfs(i, -group)  # 그룹값을 -1로 주어 dfs를 돈다.
            if not a:  # 만약 a가 false가 나왔다면
                return False  # False를 리턴
        elif visited[i] == visited[V]:  # 만약 현재 정점과 연결된 정점의 그룹값이 같다면
            return False  # False를 리턴
    return True  # 그외의 경우는 True를 리턴


for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크
    global result

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, dfs 수행
            result = dfs(i, 1)
            if not result:  # 만약 result가 False가 나왔다면 더이상 수행할 필요가 없으므로
                break  # break

    print('YES' if result else 'NO')
import sys
from collections import deque

input = sys.stdin.readline
ans = []


def dfs(node, visited, graph):
    if visited[node]:
        return
    visited[node] = True
    ans.append(node)

    for element in graph[node]:
        if not visited[element]:
            dfs(element, visited, graph)


def solve(n, graph, order):
    visited = [False for i in range(n + 1)]

    # 우선순위리스트 생성
    rank = [-1 for i in range(n + 1)]

    # 우선순위순서 계산
    for i in range(1, n + 1):
        rank[order[i - 1]] = i

    # 계산한 우선순위순서에 따라 그래프의 인접리스트 순서 정렬
    for i in range(1, n + 1):
        graph[i] = sorted(graph[i], key=lambda x: rank[x])

    # 만들어진 그래프를 DFS 탐색하고 ans와 비교
    dfs(1, visited, graph)
    if ans == order:
        print(1)
    else:
        print(0)


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(1, n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

order = list(map(int, input().split()))

solve(n, graph, order)

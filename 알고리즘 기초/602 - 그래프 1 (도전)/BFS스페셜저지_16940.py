import sys
from collections import deque

input = sys.stdin.readline
ans = []

'''
같은 BFS를 수행하더라도, 그래프 인접리스트에 정점이 어떤 순서로 들어가있냐에 따라 순회 순서가 달라질 수 있음
but 모든 순회 순서를 고려X
-> 주어진 BFS 순회 결과로부터 역으로 순회 순서를 도출한 뒤 다시 BFS를 수행해서 순회 결과와 동일한지 확인!
'''


def bfs(n, graph, order):
    visited = [False for _ in range(n + 1)]
    q = deque()

    q.append(1)
    visited[1] = True

    # 우선순위리스트
    rank = [-1 for _ in range(n + 1)]

    # 우선순위순서 계산
    for i in range(1, n + 1):
        rank[order[i - 1]] = i

    # 계산한 우선순위순서에 따라 그래프의 인접리스트 순서 정렬
    for i in range(1, n + 1):
        graph[i] = sorted(graph[i], key=lambda x: rank[x])

    # 만들어진 그래프를 BFS 탐색하고 ans와 비교
    while q:
        front = q.popleft()
        ans.append(front)

        for element in graph[front]:
            if not visited[element]:
                visited[element] = True
                q.append(element)

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

bfs(n, graph, order)

import sys

def dfs(idx, depth):
    if depth == 4: # 0부터 시작하므로 4까지
        print(1)
        exit()

    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


n, m = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n)]
visited = [False] * n

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)

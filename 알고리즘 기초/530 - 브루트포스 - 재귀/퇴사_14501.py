import sys

n = int(sys.stdin.readline())
s = [list(map(int, input().split())) for i in range(n)]
result = [0]
# 0을 넣어야 max 함수를 사용할 때 value error가 나오지 않는다.
# 경우의 수가 아예 없을 수도 있기 때문에


def solve(day, p):
    global result

    for i in range(day, n):
        # 퇴사일을 초과하지 않으면
        if i + s[i][0] <= n:
            # 재귀로 탐색
            result.append(solve(i + s[i][0], p + s[i][1]))
    return p


solve(0, 0)
print(max(result))

'''
첫 날부터 시작하여 퇴사일을 초과하지 않는 모든 경우의 수를 다 찾는다. 
그 경우의 수들 중, 가장 높은 값을 출력하면 된다.
'''
import sys

k = int(sys.stdin.readline())
sign = list(map(str, sys.stdin.readline().split()))
visitied = [False] * 11
lst = []

# 새로운 숫자가 추가 될때 마다 앞에 숫자랑 비교해주는 함수
def possible(i, j, sign):
    if sign == '>':
        return i > j
    else:
        return i < j


# 백트래킹 이용
def solve(depth, s):
    global minResult, maxResult

    if depth == k + 1:
        lst.append(s)
        return

    for i in range(10):
        if not visitied[i]:
            if depth == 0 or possible(s[len(s) - 1], str(i), sign[depth - 1]):
                visitied[i] = True
                solve(depth + 1, s + str(i))
                visitied[i] = False

solve(0, "")
print(lst[-1])  # 마지막으로 구해진 문자열이 가장 큰 문자열
print(lst[0])   # 0부터 시작하면서 커지는 순서이므로 처음 생성된 문자열이 제일 작은 문자열
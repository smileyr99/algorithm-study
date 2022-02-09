import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

button = list(map(int, input().split()))

cnt = abs(100 - n)

for i in range(1000001):
    tmp = list(str(i))
    flag = False
    # 숫자중에 못누르는 버튼이 있으면 통과
    for j in tmp:
        if int(j) in button:
            flag = True
            break
    if flag:
        continue
    # 가장 가까운 버튼 중에서 n-i 한 값 + 길이(가장 가까운 위치만큼 리모콘 누르기때문)
    else:
        cnt = min(cnt, abs(n - i) + len(str(i)))

print(cnt)


"""
풀이
처음 cnt 값을 n과 100 차이 값으로 잡고 min값을 비교해나감.

범위를 1000001 를 잡은 이유는
n이 최대 500000 일때 만약 위에서부터 ex) 600000 꺼꾸로 내려오는 경우가
더 가까운 경우가 있을수도 있어서 1000001로 잡음

for 문에서
flag로 못누르는 버튼이 있다면 통과
전부 다 누를 수 있다면 n값과의 차 + i의 길이(i값을 받기위해 리모콘을 눌렀기때문)
"""
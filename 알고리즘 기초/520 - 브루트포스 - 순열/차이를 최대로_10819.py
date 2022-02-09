import itertools

N = int(input())

nums = list(map(int, input().split()))
result = 0  # 결과 값을 저장할 result 값 선언


def result_solve(arr):  # 리스트의 차를 구하는 함수
    global result
    sub = 0  # 각 원소의 차를 저장
    for i in range(len(arr) - 1):
        sub += abs(arr[i] - arr[i + 1])  # 각 원소의 차의 절대값을 계속해서 더해나간다.

    result = max(result, sub)    # 저장되어있는 결과값과 비교해서 큰 값을 결과값에 대입


for i in itertools.permutations(nums, N):   # permutations 라이브러리 이용(입력받은 리스트의 원소중에서 N개를 뽑는다.)
    result_solve(i)  # 뽑은 순열마다 리스트의 차를 구하여 result에 대입

print(result)

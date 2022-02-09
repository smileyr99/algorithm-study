import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
flag = False

for i in range(n-1, 0, -1):     # 마지막 항부터 돈다
    if nums[i-1] > nums[i]:     # 만약 앞 열의 값이 그 뒷열의 값보다 크다면
        for j in range(n-1, 0, -1):     # 다시 그 앞 열의 값을 맨 뒷열부터 비교
            if nums[i-1] > nums[j]:     # 뒤 열값 중 그 앞열의 값보다 작은 값이 있다면
                nums[i-1], nums[j] = nums[j], nums[i-1]  # 그 두 값을 스왑
                nums = nums[:i] + sorted(nums[i:], reverse= True)      # i-1 번째 까지의 리스트와 그 뒤에리스트를 오름차순으로 정렬한 채로 붙인다.
                print(*nums)    # *를 이용해 리스트 내부의 원소들을 공백을 사용하여 출력
                exit()      # 코드 종료

print(-1)   # 만약 위에서 코드 종료가 일어나지 않았다면(마지막 항이라면) -1 출력
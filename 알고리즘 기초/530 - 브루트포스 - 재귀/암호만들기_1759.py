L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()  # 알파벳 오름차순 정렬(증가하는 순서로 배열된다하므로)
vowel = ['a', 'e', 'i', 'o', 'u']  # 모음 세팅
out = []

# 백트래킹 방법
def solve(depth, idx):
    # 길이 l 인 경우이면서 모음이 최소 1개, 자음이 최소 2개인 경우 출력
    if depth == L:
        vo = 0  # 모음 개수
        co = 0  # 자음 개수
        for i in range(len(out)):
            if out[i] in vowel:  # 출력할 알파벳에 모음이 있는지 없는지 체크
                vo += 1  # 모음이 있으면 +1
            else:  # 모음이 아니라면
                co += 1  # 자음에 +1
        if vo >= 1 and co >= 2:  # 모음이 1개 이상이고 자음이 2개 이상이라면
            print(''.join(out))  # 출력
        return

    # DFS를 통해 l 길이만큼의 암호를 만듬
    for i in range(idx, C):
        out.append(alphabet[i])  # 출력 리스트에 추가
        solve(depth + 1, i + 1)  # 재귀를 돈다
        out.pop()  # 출력 함수에서 제거


solve(0, 0)
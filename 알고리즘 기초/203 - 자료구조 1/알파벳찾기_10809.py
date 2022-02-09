answer = [-1] * 26
words = [ord(i) - ord('a') for i in input()]
# words를 input으로 받으며 ASCII - ASCII(a)한 값들을 저장 ==> a의 값이 0이 되도록

# answer의 index = 알파벳의 ASCII = word의 값
for i, v in enumerate(words): # words를 돌며 해당 값의 answer index가 -1이면 Index로 바꿔줌
    if answer[v] == -1:
        answer[v] = i

print(*answer)


import sys

string = list(sys.stdin.readline().strip())
tag = False
result = ""
stack = ""

# <, > 안에 있는 문자열은 그대로 출력하고, 그 밖에 있는 문자들을 스택에 담음.
# 공백이 있을 경우 스택에 담았던 문자열을 뒤집어 출력.
for i in string:
    if i == '<':
        tag = True
        result += stack[::-1]
        stack = ""
        result += i
        continue
    elif i == '>':
        tag = False
        result += i
        continue
    elif i == " ":
        result += stack[::-1] + " "
        stack = ""
        continue

    if tag:
        result += i
    else:
        stack += i

print(result + stack[::-1])


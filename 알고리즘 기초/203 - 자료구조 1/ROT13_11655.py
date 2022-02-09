import sys

s = input()
encode = ''

for i in s:
    if i.isalpha():
        if 'a' <= i <= 'm' or 'A' <= i <= 'M':
            encode += (chr(ord(i)+13))
        elif 'n' <= i <= 'z' or 'N' <= i <= 'Z':
            encode += (chr(ord(i)-13))
    else:
        encode += i

print(encode)
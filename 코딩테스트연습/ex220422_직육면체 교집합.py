# 백준 11665번
answer = ''

for i in s:
    if i.islower():
            if 97 <= ord(i) <= 109:
                answer += chr(ord(i) + 13)
            else:
                answer += chr(ord(i) - 13)
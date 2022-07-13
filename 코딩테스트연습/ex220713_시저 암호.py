# programmers 12926
def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr(ord(i)+n) if ord(i)+n<91 else chr(ord(i)+n-26)
        elif i.islower():
            answer += chr(ord(i)+n) if ord(i)+n<123 else chr(ord(i)+n-26)
        elif i == ' ':
            answer += i         
    return answer
print(solution('z Z a A',1))

# def solution(s, n):
#     s = list(s) 
#     for i in range(len(s)): 
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
#     return "".join(s)
# print(solution('z Z a A',1))
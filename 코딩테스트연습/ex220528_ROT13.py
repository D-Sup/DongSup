# baekjoon 11655
N = input()
M = []
for i in range(len(N)): 
    if int(ord(N[i])+13) >= 123 or 96>= int(ord(N[i])+13) >= 91:
        M.append(chr(int(ord(N[i])-13)))
    elif 57 >= int(ord(N[i])) >= 48:
        M.append(N[i])
    else: 
        M.append(chr(int(ord(N[i])+13)))
M = "".join(M)
print(M.replace("-"," "))     

# s = input()
# res = ''
# for c in s:
#     if 'a' <= c <= 'z':
#         res += chr((ord(c)+13) if c <= 'm' else ord(c)-13)
#     elif 'A' <= c <= 'Z':
#         res += chr((ord(c)+13) if c <= 'M' else ord(c)-13)
#     else:
#         res += c
# print(res)
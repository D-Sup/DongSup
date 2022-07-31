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

# N = input()
# result = ''
# for i in N:
#     if 'a' <= i <= 'z':
#         result += chr(ord(i)+13) if i < 'm' else chr(ord(i)-13)
#     elif 'A' <= i <= 'Z':
#         result += chr(ord(i)+13) if i < 'M' else chr(ord(i)-13)
#     else:
#         result += i
# print(result)  

# new method
# s = [ord(x) for x in input('')]
# r = ''
# for ss in s:
#     if ss > 96 and ss < 123:
#         r += chr(ss + 13) if ss < 110 else chr(ss - 13)
#     elif ss > 64 and ss < 91:
#         r += chr(ss + 13) if ss < 78 else chr(ss - 13)
#     else:
#         r += chr(ss)
# print(r)
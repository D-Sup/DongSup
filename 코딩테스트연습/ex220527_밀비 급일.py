# baekjoon 11365
M = []
def add():
    while 1:
        M.append("".join(reversed(input())))
        if M[-1] == "DNE":
            del(M[-1])
            return M
add()
print(*M,sep='\n')

# new method
# while 1:
#     N = input()
#     if N == 'END':
#         break
#     print(N[::-1])
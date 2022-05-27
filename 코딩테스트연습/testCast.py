# # baekjoon 
# M = [p for p in range(1,15)]
# N = [q for q in range(1,15)]


# for i in M[::4]:
#     N[i] = 4
# print(N)

# baekjoon 
M = [p for p in range(0,16)]
S = 100

for i in M[3::5]:
    S +=1
    M[i] = S
print(M)
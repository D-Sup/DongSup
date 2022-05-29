# baekjoon 1676
h = 1
R = 0
for i in range(int(input()),1,-1):
    h*=i
M = str(h)
for j in M[::-1]:
    if j == '0':
        R+=1
    else:
        print(R)
        break
# baekjoon 11653
N = int(input()) 
r = 2  
while N != 1:
    if N % r != 0:
        r += 1
    else:
        N //= r
        print(r)
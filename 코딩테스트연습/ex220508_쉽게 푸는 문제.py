# baekjoon 1292
import sys
input = sys.stdin.readline
a, b = map(int,input().split())
sequence = [0,]
for i in range(1,100):
    for _ in range(i):
        sequence.append(i)
print(sum(sequence[a:b+1]))
        
# import sys
# input = sys.stdin.readline
# sequence = [[i]*i for i in range(1,46)]
# a, b = map(int,input().split())
# sequence = [0] + sum(sequence,[])
# print(sum(sequence[a:b+1]))
# print(sequence[a:b+1])

# 백준 17249번
import sys
sys.stdin = open("input.txt", 'r')

i = 0
r = [0, 0]
for c in input():
    if c == '@':
        r[i] += 1
    elif c == '(':
        i ^= 1
print(*r)
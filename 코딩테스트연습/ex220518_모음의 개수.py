# baekjoon 10987
import sys
input = sys.stdin.readline
r = 0
N = list(input())
vow = ['a','e','i','o','u']
for i in N:
    if i in vow:
        r += 1
print(r)
# baekjoon 11721
import sys
input = sys.stdin.readline
N = list(map(str,input()))
del(N[-1])
N.insert(0,0)
for i in range(1,len(N)):
    print(N[i],end='')
    if i%10 == 0 and i >= 10 :
        print()

# new method
s = input()
for i in range(len(s)):
    print(s[i] + '\n' if i % 10 == 9 else s[i], end='')
# baekjoon 10809
import sys
input = sys.stdin.readline
str = input()
string = 'abcdefghijklmnopqrstuvwxyz'
for i in string:
    if i in str:
        print(str.index(i),end=' ')
    else:
        print(-1,end=' ')

# import sys
# input = sys.stdin.readline
# N = input()
# M = list(range(97,123))
# for i in M:
#     print(N.find(chr(i)))
    
# https://ooyoung.tistory.com/78